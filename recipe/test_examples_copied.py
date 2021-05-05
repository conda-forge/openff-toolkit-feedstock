"""Test that examples copied to CONDA_PREFIX by move-examples.sh are correct"""

from pathlib import Path
from os import environ
from sys import stderr


def file_tree(path):
    """Get the entire tree of real files at path, sorted into a list"""
    return sorted([p for p in Path(path).glob("**") if p.is_file()])


def main():
    """Entrypoint for this test"""
    repo_path = Path("examples")
    installed_path = Path(environ["CONDA_PREFIX"]) / "share/openff-toolkit/examples"

    repo_tree = file_tree(repo_path)
    installed_tree = file_tree(installed_path)

    print("Source repository examples tree:", *repo_tree, sep="\n    ")
    print("Installed examples tree:", *installed_tree, sep="\n    ")
    print("This message was sent to stderr, can you see it in Azure?", file=stderr)

    assert repo_tree
    assert repo_tree == installed_tree


if __name__ == "__main__":
    main()
