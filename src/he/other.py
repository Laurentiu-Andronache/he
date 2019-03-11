"""Helpers that don't fit specifically in any of the other modules."""

import subprocess
from os import PathLike
from typing import Union, Sequence, Text, Any


#
# from pydbg import dbg


def run(
        shell_command: Union[bytes, Text, Sequence[Union[bytes, Text, PathLike]]],  # type: ignore
        **subprocess_run_kwargs: Any,
) -> int:
    """Run one or more commands in the local shell.

    WARNING: Make sure that user input cannot get in any way as an argument to this function!
    """
    try:
        return subprocess.run(
            shell_command, check=True, shell=True, **subprocess_run_kwargs
        ).returncode
    except subprocess.CalledProcessError as e:
        return e.returncode

#
# if __name__ == '__main__':
#     dbg(run('dir'))
#     dbg(run('dir /?'))
#     dbg(run(['dir', 'other.py']))
#     dbg(run(['dir', os.getcwd()]))
