#!/bin/sh
# wait.sh
set -e

# wait for postgres to boot up
# it's really "naive" way to "sync"
sleep 2
exec $@
