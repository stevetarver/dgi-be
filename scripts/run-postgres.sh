#!/bin/sh -e
#
# Run our postgres container for local development
#
# Our compose file uses a local directory for PGDATA so that data persists
# through container restarts.
#
# Use this script to ensure the PGDATA exists and the relative path is correct.
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
    # We operate from the 'docker' directory
    cd ${THIS_SCRIPT_DIR}/../docker

    if ! [ -d 'pgdata' ]; then
        mkdir pgdata
    fi

    docker-compose -f postgres-compose.yaml up -d
)



