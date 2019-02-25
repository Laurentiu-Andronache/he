"""Helpers that can be used to decorate functions."""

import logging
from functools import wraps
from time import perf_counter


def timer(func):
    """Calculates the runtime of a function, and outputs it to logging.DEBUG."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter()
        _logger = logging.getLogger(__name__ + '.' + func.__name__)
        _logger.debug(' runtime: {:.4f} seconds'.format(end - start))
        return value

    return wrapper


def debug(func):
    """Outputs to logging.DEBUG the function arguments and return value."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        _logger = logging.getLogger(__name__ + '.' + func.__name__)
        _logger.debug(' called with args (%s)', signature)
        value = func(*args, **kwargs)
        _logger.debug(' returned %r', value)
        return value

    return wrapper


@debug
def enjoy_decorators():
    """Enjoy seeing what the decorators from this file in action."""

    from time import sleep

    sleep = debug(sleep)

    @timer
    def sleep_times(time, times):
        val = time * times
        sleep(val)
        return val

    sleep_times(0.1, 2)

    return 1337


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    exit(enjoy_decorators())
