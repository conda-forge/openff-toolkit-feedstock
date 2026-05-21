#! /bin/bash

# Shell safety: Exit script on error, treat unset variables as error, propagate errors out of pipelines
set -eu -o pipefail

echo "CONDA_PREFIX_2 is: "
echo $CONDA_PREFIX_2

env

mkdir -p "$CONDA_PREFIX_2/share/openff-toolkit"
cp -r examples "$CONDA_PREFIX_2/share/openff-toolkit"

mkdir -p "$CONDA_PREFIX_2/bin"
mv "$CONDA_PREFIX_2/share/openff-toolkit/examples/examples_helper.py" "$CONDA_PREFIX_2/bin/openff-toolkit-examples"
chmod +x "$CONDA_PREFIX_2/bin/openff-toolkit-examples"
