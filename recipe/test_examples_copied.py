"""Test that examples copied to CONDA_PREFIX by move-examples.sh are correct"""

from pathlib import Path
from os import environ


def file_tree(path):
    """Get the entire tree of files at path, sorted into a list"""
    root = Path(path)
    return sorted([p.relative_to(root) for p in root.glob("**/*")])


def main():
    """Entrypoint for this test"""
    repo_path = Path("examples")
    installed_path = Path(environ["CONDA_PREFIX"]) / "share/openff-toolkit/examples"

    repo_tree = file_tree(repo_path)
    installed_tree = file_tree(installed_path)

    print("Source repository examples tree:", *repo_tree, sep="\n    ")
    print("Installed examples tree:", *installed_tree, sep="\n    ")

    assert repo_tree, "Source repository tree is empty"
    assert (
        repo_tree == installed_tree
    ), "Source repository tree doesn't match installed tree"


if __name__ == "__main__":
    main()
