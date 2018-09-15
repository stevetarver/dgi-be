#!/bin/sh -e
#
# Run mypy to check type annotations
#
# CAVEATS:
#   Our directory locator will not reliably work on a mac when this
#   script is called through a symlink
#
# TODO:
#   Figure out a robust directory locator for a symlink on mac.
#   Researched readlink & stat & google and found no solution but
#   'brew install coreutils' and greadlink.
#
if [ "$(uname -s)" = "Darwin" ]; then
    # If called through a symlink, this will point to the symlink
    THIS_SCRIPT_DIR="$( cd "$( dirname "${0}" )" && pwd )"
else
    THIS_SCRIPT_DIR=$(dirname $(readlink -f "${0}"))
fi
(
    cd ${THIS_SCRIPT_DIR}/..

    black --include .py$ src
)



