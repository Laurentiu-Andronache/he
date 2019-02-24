from os import chdir
from pathlib import Path

import pytest

from he.contexts import working_directory


def test_working_directory_with_absolute_path(tmp_path):
    for temp_dir in (tmp_path, str(tmp_path), 1337):
        initial_path = Path.cwd()

        @working_directory(temp_dir)
        def with_decorator():
            return Path.cwd()

        if isinstance(temp_dir, int):
            with pytest.raises(TypeError):
                with_decorator()
        else:
            assert Path(temp_dir) == with_decorator()
            assert Path.cwd() == initial_path


def test_working_directory_with_relative_path():
    initial_path_dir = Path.cwd()
    temp_relative_dir = 'temp-test-dir'
    relative_dir_path = Path(temp_relative_dir).absolute()
    if not relative_dir_path.exists():
        relative_dir_path.mkdir()

    # to make it more difficult, changing the actual working directory...
    chdir(Path.home())

    # ... but we'll test the function with a path relative to the initial working directory (initial_path)
    @working_directory(temp_relative_dir, initial_path_dir)
    def with_decorator():
        return Path.cwd()

    assert relative_dir_path == with_decorator()
    assert Path.cwd() == initial_path_dir

    # also try with initial_path as file instead of directory
    initial_path_file = Path.cwd() / 'fictive_calling_script.py'

    @working_directory(temp_relative_dir, initial_path_file)
    def again_with_decorator():
        return Path.cwd()

    assert relative_dir_path == again_with_decorator()
    assert Path.cwd() == initial_path_dir

    # cleanup
    if relative_dir_path.exists():
        relative_dir_path.rmdir()
