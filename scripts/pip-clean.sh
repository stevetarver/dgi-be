#!/bin/sh -e
#
# Remove all packages from our python environment
#
# Use to prove requirements files, or clean-slate to remove unwanted packages
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

    pip freeze | xargs pip uninstall -y
)
