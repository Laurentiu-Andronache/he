from he.other import run


def test_run():
    assert 1 == run('non-existent-command', capture_output=True)
    assert 0 == run('dir', capture_output=True)
