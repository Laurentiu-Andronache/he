from time import sleep

from he.decorators import timer, debug


def test_timer(caplog):
    caplog.set_level(0)

    @timer
    def sleep_one_second():
        sleep(0.1)

    sleep_one_second()
    assert sleep_one_second.__name__ == 'sleep_one_second'
    assert caplog.record_tuples

    logged_message = caplog.messages[0]
    time_str = logged_message.split()[1]
    time_rounded = round(float(time_str), 2)
    assert 0.1 == time_rounded


def test_debug(caplog):
    caplog.set_level(0)

    @debug
    def add(val1, val2=855):
        return val1 + val2

    add(482)
    assert caplog.messages[0] == ' called with args (482)'
    assert caplog.messages[1] == ' returned 1337'
