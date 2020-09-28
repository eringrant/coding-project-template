#!/bin/bash
# Execute with `source setup_env.sh`.

export PYTHONPATH=$(pwd):$PYTHONPATH  # add path for current module
SUBMODULES=  # space-separateed list: "SUBMODULE1 SUBMODULE2 ..."
for submodule in $SUBMODULES
do
    export PYTHONPATH=$(pwd)/${submodule}:$PYTHONPATH  # add paths for submodules
done