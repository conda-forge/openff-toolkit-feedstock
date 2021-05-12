mkdir -p $CONDA_PREFIX/share/openff-toolkit
cp -r examples $CONDA_PREFIX/share/openff-toolkit

mv $CONDA_PREFIX/share/openff-toolkit/examples/examples_helper.py $CONDA_PREFIX/bin/openff-toolkit-examples
chmod +x $CONDA_PREFIX/bin/openff-toolkit-examples
