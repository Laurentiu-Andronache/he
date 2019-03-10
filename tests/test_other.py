from he.other import run


def test_run():
    ret_err = run('non-existent-command', capture_output=True)
    assert isinstance(ret_err, int)
    assert ret_err != 0
    assert 0 == run('dir', capture_output=True)
