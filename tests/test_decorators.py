import time

import pytest

from he.decorators import (
    timer,
    debug,
    throttle,
    singleton,
    repeat,
    count_calls,
    CountCalls,
)


# GIVEN any decorator
@pytest.mark.parametrize(
    'decorator',
    [timer, debug, throttle(rate=0.01), singleton, repeat, count_calls, CountCalls],
)
def test_consistency(decorator):
    # WHEN decorating a function
    @decorator
    def nothing(arg, *, kwarg=5):
        """nothing's docstring"""
        return arg + kwarg

    # THEN the function's identity is preserved
    assert 'nothing' == nothing.__name__
    assert "nothing's docstring" == nothing.__doc__

    # THEN the function's return value is returned, and its arguments are preserved
    assert 1337 == nothing(1269, kwarg=68)


def test_timer(caplog):
    caplog.set_level(0)

    @timer
    def sleep_one_second():
        time.sleep(0.1)

    sleep_one_second()

    assert caplog.record_tuples

    logged_message = caplog.messages[0]
    time_str = logged_message.split()[1]
    time_rounded = round(float(time_str), 1)
    assert 0.1 == time_rounded


def test_debug(caplog):
    caplog.set_level(0)

    @debug
    def add(val1, val2=855):
        return val1 + val2

    add(482)
    assert caplog.messages[0] == ' called with args (482)'
    assert caplog.messages[1] == ' returned 1337'


# Test missing: decorator `throttle` without argument; not doing it because 1 second would be too long for a test.
def test_throttle():
    # GIVEN a function that shouldn't get called more often than once every 0.1 seconds
    @throttle(rate=0.1)
    def nothing():
        pass

    # WHEN it gets called two times
    start = time.time()
    nothing()
    nothing()
    end = time.time()

    # THEN around 0.2 seconds have passed
    execution_time = end - start
    assert 0.2 == round(execution_time, 1)


def test_singleton():
    # GIVEN a class that shouldn't be instantiated more than once
    @singleton
    class Single:
        def __init__(self, value):
            self.value_initializable_once = value

    # WHEN the user tries to instantiate it more than once
    class_1 = Single('initialization text')
    class_2 = Single("different text that shouldn't get used")

    # THEN all instances actually refer to the same initial instance
    assert class_1 is class_2
    assert 'initialization text' == class_2.value_initializable_once


def test_repeat():
    # GIVEN a function that should run three times for each call directive
    @repeat
    def nothing_three_times():
        nothing_three_times.counter += 1

    nothing_three_times.counter = 0

    # WHEN it got called once
    nothing_three_times()

    # THEN it actually ran three times
    assert 3 == nothing_three_times.counter

    # And now the same test with an argument on the decorator...
    @repeat(num_times=4)
    def nothing_four_times():
        nothing_four_times.counter += 1

    nothing_four_times.counter = 0

    nothing_four_times()

    assert 4 == nothing_four_times.counter


def test_count_calls(caplog):
    caplog.set_level(level=0)

    @count_calls
    def nothing():
        pass

    for _ in range(5):
        nothing()

    assert 5 == len(caplog.record_tuples)
    assert '5 times' in caplog.record_tuples[4][2]
    assert 5 == nothing.num_calls


def test_CountCalls(caplog):
    caplog.set_level(level=0)

    @CountCalls
    def nothing():
        pass

    for _ in range(5):
        nothing()

    assert 5 == len(caplog.record_tuples)
    assert '5 times' in caplog.record_tuples[4][2]
    assert 5 == nothing.num_calls
