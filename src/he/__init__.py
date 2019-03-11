"""`he` is a library of Python helpers.

Documentation:      https://he.readthedocs.io
Code Repository:    https://github.com/Laurentiu-Andronache/he
"""
from pathlib import Path


def main() -> None:  # pragma: no cover
    """Entry point for the application script."""
    print(f'Your working directory is {Path.cwd()}')
