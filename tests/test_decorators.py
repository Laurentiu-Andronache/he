from time import sleep

from he.decorators import timer


def test_timer(caplog):
    caplog.set_level(0)

    @timer
    def sleep_one_second():
        sleep(0.01)

    sleep_one_second()
    assert sleep_one_second.__name__ == 'sleep_one_second'
    assert '0.01' in caplog.text
