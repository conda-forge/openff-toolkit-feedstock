"""Test that examples copied to CONDA_PREFIX by move-examples.sh are correct"""

from pathlib import Path
from os import environ
from subprocess import run


def file_tree(path):
    """Get the entire tree of files at path, sorted into a list"""
    root = Path(path)
    return sorted([p.relative_to(root) for p in root.glob("**/*")])


def main():
    """Entrypoint for this test"""
    # Get lists of the examples files in source and installation
    repo_tree = file_tree("examples")
    installed_tree = file_tree(
        Path(environ["CONDA_PREFIX"]) / "share/openff-toolkit/examples"
    )

    # Print the trees out for debugging
    print("Source repository examples tree:", *repo_tree, sep="\n    ")
    print("Installed examples tree:", *installed_tree, sep="\n    ")

    # Remove the helper script, which is moved to the bin directory during installation
    repo_tree.remove(Path("examples_helper.py"))

    # Check that the (filtered) file trees match, and are not empty
    assert repo_tree, "Source repository tree is empty"
    assert repo_tree == installed_tree, "Source repo tree doesn't match installed tree"

    # Run the examples helper and check what files it copies over
    helper_test_path = Path("helper_test_target")
    helper_test_path.mkdir()
    run(
        ["openff-toolkit-examples", "--include-deprecated"],
        cwd=helper_test_path,
        check=True,
    )
    helper_test_tree = file_tree(helper_test_path / "examples")

    # Print and check the helper test
    print("Examples helper target tree:", *helper_test_tree, sep="\n    ")
    assert helper_test_tree == repo_tree, "Examples helper failed to install all files"


if __name__ == "__main__":
    main()
