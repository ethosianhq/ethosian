#!/bin/bash

############################################################################
#
# Release ethosian to pypi
# Usage:
#   ./scripts/release.sh
#
# Note:
#   build & twine must be available in the venv
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$( dirname ${CURR_DIR} )"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Releasing *ethosian*"

  cd ${REPO_ROOT}
  print_heading "pwd: $(pwd)"

  print_heading "Proceed?"
  space_to_continue

  print_heading "Building ethosian"
  python3 -m build

  print_heading "Release ethosian to testpypi?"
  space_to_continue
  python3 -m twine upload --repository testpypi ${REPO_ROOT}/dist/*

  print_heading "Release ethosian to pypi"
  space_to_continue
  python3 -m twine upload --repository pypi ${REPO_ROOT}/dist/*
}

main "$@"
