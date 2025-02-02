#!/bin/bash

############################################################################
#
# This script tests the ethosian codebase
# Usage:
#   ./scripts/test.sh
#
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$( dirname ${CURR_DIR} )"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Testing ethosian"
  print_heading "Running: pytest ${REPO_ROOT}"
  pytest ${REPO_ROOT}
}

main "$@"
