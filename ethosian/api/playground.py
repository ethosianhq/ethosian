from os import getenv
from pathlib import Path
from typing import Union, Dict, List

from httpx import Response, Client as HttpxClient

from ethosian.constants import ethosian_API_KEY_ENV_VAR
from ethosian.cli.settings import ethosian_cli_settings
from ethosian.cli.credentials import read_auth_token
from ethosian.api.api import api, invalid_response
from ethosian.api.routes import ApiRoutes
from ethosian.api.schemas.playground import PlaygroundEndpointCreate
from ethosian.utils.log import logger


def create_playground_endpoint(playground: PlaygroundEndpointCreate) -> bool:
    logger.debug("--**-- Creating Playground Endpoint")
    with api.AuthenticatedClient() as api_client:
        try:
            r: Response = api_client.post(
                ApiRoutes.PLAYGROUND_ENDPOINT_CREATE,
                json={"playground": playground.model_dump(exclude_none=True)},
            )
            if invalid_response(r):
                return False

            response_json: Union[Dict, List] = r.json()
            if response_json is None:
                return False

            # logger.debug(f"Response: {response_json}")
            return True
        except Exception as e:
            logger.debug(f"Could not create Playground Endpoint: {e}")
    return False


def deploy_playground_archive(name: str, tar_path: Path) -> bool:
    """Deploy a playground archive.

    Args:
        name (str): Name of the archive
        tar_path (Path): Path to the tar file

    Returns:
        bool: True if deployment was successful

    Raises:
        ValueError: If tar_path is invalid or file is too large
        RuntimeError: If deployment fails
    """
    logger.debug("--**-- Deploying Playground App")

    # Validate input
    if not tar_path.exists():
        raise ValueError(f"Tar file not found: {tar_path}")

    # Check file size (e.g., 100MB limit)
    max_size = 100 * 1024 * 1024  # 100MB
    if tar_path.stat().st_size > max_size:
        raise ValueError(f"Tar file too large: {
                         tar_path.stat().st_size} bytes (max {max_size} bytes)")

    # Build headers
    headers = {}
    if token := read_auth_token():
        headers[ethosian_cli_settings.auth_token_header] = token
    if ethosian_api_key := getenv(ethosian_API_KEY_ENV_VAR):
        headers["Authorization"] = f"Bearer {ethosian_api_key}"

    try:
        with (
            HttpxClient(base_url=ethosian_cli_settings.api_url, headers=headers) as api_client,
            open(tar_path, "rb") as file,
        ):
            files = {"file": (tar_path.name, file, "application/gzip")}
            r: Response = api_client.post(
                ApiRoutes.PLAYGROUND_APP_DEPLOY,
                files=files,
                data={"name": name},
            )

            if invalid_response(r):
                raise RuntimeError(f"Deployment failed with status {
                                   r.status_code}: {r.text}")

            response_json: Dict = r.json()
            logger.debug(f"Response: {response_json}")
            return True

    except Exception as e:
        raise RuntimeError(f"Failed to deploy playground app: {str(e)}") from e
