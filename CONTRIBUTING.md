# Contributing to ethosian

ethosian is an open-source project and we welcome contributions.

## 👩‍💻 How to contribute

Please follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow:

- Fork the repository.
- Create a new branch for your feature.
- Add your feature or improvement.
- Send a pull request.
- We appreciate your support & input!

## Development setup

1. Clone the repository.
2. Create a virtual environment:
   - For Unix, use `./scripts/create_venv.sh`.
   - For Windows, use `.\scripts\create_venv.bat`.
   - This setup will:
     - Create a `ethenv` virtual environment in the current directory.
     - Install the required packages.
     - Install the `ethosian` package in editable mode.
3. Activate the virtual environment:
   - On Unix: `source ethenv/bin/activate`
   - On Windows: `ethenv\Scripts\activate`

## Formatting and validation

Ensure your code meets our quality standards by running the appropriate formatting and validation script before submitting a pull request:

- For Unix:
  - `./scripts/format.sh`
  - `./scripts/validate.sh`
- For Windows:
  - `.\scripts\format.bat`
  - `.\scripts\validate.bat`

These scripts will perform code formatting with `ruff`, static type checks with `mypy`, and run unit tests with `pytest`.

## Adding a new Vector Database

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `ethosian/vectordb` for the new vector database.
3. Create a Class for your VectorDb that implements the `VectorDb` interface
   - Your Class will be in the `ethosian/vectordb/<your_db>/<your_db>.py` file.
   - The `VectorDb` interface is defined in `ethosian/vectordb/base
   - Import your `VectorDb` Class in `ethosian/vectordb/<your_db>/__init__.py`.
   - Checkout the [`ethosian/vectordb/pgvector/pgvector`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/vectordb/pgvector/pgvector.py) file for an example.
4. Add a recipe for using your `VectorDb` under `cookbook/vectordb/<your_db>`.
   - Checkout [`ethosian/cookbook/vectordb/pgvector`](https://github.com/ethosianhq/ethosian/tree/main/cookbook/vectordb/pgvector) for an example.
5. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
6. Submit a pull request.

## Adding a new Model Provider

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `ethosian/model` for the new Model provider.
3. If the Model provider supports the OpenAI API spec:
   - Create a Class for your LLM provider that inherits the `OpenAILike` Class from `ethosian/model/openai/like.py`.
   - Your Class will be in the `ethosian/model/<your_model>/<your_model>.py` file.
   - Import your Class in the `ethosian/model/<your_model>/__init__.py` file.
   - Checkout the [`ethosian/model/xai/xai.py`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/llm/together/together.py) file for an example.
4. If the Model provider does not support the OpenAI API spec:
   - Checkout [`ethosian/model/anthropic/claude.py`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/model/anthropic/claude.py) or [`ethosian/model/cohere/chat.py`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/model/cohere/chat.py) for inspiration.
5. Add a recipe for using your Model provider under `cookbook/providers/<your_model>`.
   - Checkout [`ethosian/cookbook/provider/claude`](https://github.com/ethosianhq/ethosian/tree/main/cookbook/providers/claude) for an example.
6. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
7. Submit a pull request.

## Adding a new Tool.

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `ethosian/tools` for the new Tool.
3. Create a Class for your Tool that inherits the `Toolkit` Class from `ethosian/tools/toolkit/.py`.
   - Your Class will be in `ethosian/tools/<your_tool>.py`.
   - Make sure to register all functions in your class via a flag.
   - Checkout the [`ethosian/tools/youtube_tools.py`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/tools/youtube_tools.py) file for an example.
   - If your tool requires an API key, checkout the [`ethosian/tools/serpapi_tools.py`](https://github.com/ethosianhq/ethosian/blob/main/ethosian/tools/serpapi_tools.py) as well.
4. Add a recipe for using your Tool under `cookbook/tools/<your_tool>`.
   - Checkout [`ethosian/cookbook/tools/youtube_tools`](https://github.com/ethosianhq/ethosian/blob/main/cookbook/tools/youtube_tools.py) for an example.
5. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
6. Submit a pull request.


## 📝 License

This project is licensed under the terms of the [MPL-2.0 license](/LICENSE)
