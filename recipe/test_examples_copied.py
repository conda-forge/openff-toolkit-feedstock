"""Test that examples copied to CONDA_PREFIX by move-examples.sh are correct"""

from pathlib import Path
from os import environ


def file_trees_match(left, right):
    """True if the file paths at left and right have identical contents, false otherwise"""
    a = Path(left).glob("**")
    b = Path(right).glob("**")

    return sorted(a) == sorted(b)


def is_empty(path):
    """True if the given path contains no real files"""
    return len([p for p in Path(path).glob("*") if p.is_file()]) == 0


def main():
    """Entrypoint for this test"""
    repo_examples = Path("examples")
    installed_examples = Path(environ["CONDA_PREFIX"]) / "share/openff-toolkit/examples"

    assert file_trees_match(repo_examples, installed_examples)
    assert not is_empty(installed_examples)


if __name__ == "__main__":
    main()
