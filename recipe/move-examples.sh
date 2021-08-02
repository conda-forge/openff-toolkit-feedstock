#! /bin/bash

# Shell safety: Exit script on error, treat unset variables as error, propagate errors out of pipelines
set -eu -o pipefail

mkdir -p "$CONDA_PREFIX/share/openff-toolkit"
cp -r examples "$CONDA_PREFIX/share/openff-toolkit"

mkdir -p "$CONDA_PREFIX/bin"
mv "$CONDA_PREFIX/share/openff-toolkit/examples/examples_helper.py" "$CONDA_PREFIX/bin/openff-toolkit-examples"
chmod +x "$CONDA_PREFIX/bin/openff-toolkit-examples"
