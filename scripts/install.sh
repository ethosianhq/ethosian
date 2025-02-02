#!/bin/bash

############################################################################
#
# Install ethosian
# Usage:
#   ./scripts/install.sh
#
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$( dirname ${CURR_DIR} )"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Installing ethosian"

  print_heading "Installing requirements.txt"
  pip install --no-deps \
    -r ${REPO_ROOT}/requirements.txt

  print_heading "Installing ethosian with [all] extras"
  pip install --editable "${REPO_ROOT}[all]"
}

main "$@"
