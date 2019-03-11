"""Helpers that can be used for context management."""

import logging
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Union, Iterator

_LOGGER = logging.getLogger(__name__)


@contextmanager
def working_directory(
        temporary_path: Union[Path, str],
        initial_path: Union[Path, str] = Path.cwd()
) -> Iterator[None]:
    """Change working directory, and return to `initial_path` on exit.

    It's needed for PRAW for example, because it looks for praw.ini in Path.cwd(),
    but that file could be kept in a different directory.

    `initial_path` can be used for example to change working directory relative to the script path, or
    to end up in a different directory than Path.cwd() of the calling script.

    Inspiration: https://stackoverflow.com/questions/41742317/how-can-i-change-directory-with-python-pathlib
    """
    _LOGGER.debug('Working directory of the calling script: %s', Path.cwd())
    _LOGGER.debug('temporary_path = %s', temporary_path)
    _LOGGER.debug('initial_path = %s', initial_path)

    temporary_path = Path(temporary_path)
    initial_path = Path(initial_path)

    if not initial_path.is_dir():
        initial_path = initial_path.parent

    try:
        os.chdir(initial_path / temporary_path)
        _LOGGER.debug('Temporarily changed working directory to: %s', Path.cwd())
        yield
    finally:
        os.chdir(initial_path)
