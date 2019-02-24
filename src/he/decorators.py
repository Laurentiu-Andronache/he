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
        _logger.debug('runtime: {:.4f} seconds'.format(end - start))
        return value

    return wrapper
