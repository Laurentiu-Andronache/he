"""Helpers that can be used to decorate functions."""

import functools
import logging
import time
from typing import Callable, Type, Optional, Any, cast, TypeVar, Union

F = TypeVar('F', bound=Callable[..., Any])
C = TypeVar('C', bound=Type[Any])


def timer(func: F) -> F:
    """Calculates the runtime of a function, and outputs it to logging.DEBUG."""
    _logger = logging.getLogger(__name__ + '.' + func.__name__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        return_value = func(*args, **kwargs)
        end = time.perf_counter()
        _logger.debug(' runtime: {:.4f} seconds'.format(end - start))
        return return_value

    return cast(F, wrapper)


def debug(func: F) -> F:
    """Outputs to logging.DEBUG the function arguments and return value."""
    _logger = logging.getLogger(__name__ + '.' + func.__name__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        _logger.debug(' called with args (%s)', signature)
        return_value = func(*args, **kwargs)
        _logger.debug(' returned %r', return_value)
        return return_value

    return cast(F, wrapper)


def throttle(
    _func: Optional[F] = None, *, rate: float = 1
) -> Union[F, Callable[[F], F]]:
    """Throttles a function call, so that at minimum it can be called every `rate` seconds.

    Usage::

        # this will enforce the default minimum time of 1 second between function calls
        @throttle
        def ...

    or::

        # this will enforce a custom minimum time of 2.5 seconds between function calls
        @throttle(rate=2.5)
        def ...

    This will raise an error, because `rate=` needs to be specified::

        @throttle(5)
        def ...
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time.sleep(rate)
            return func(*args, **kwargs)

        return cast(F, wrapper)

    if _func is None:
        return decorator
    return decorator(_func)


def singleton(cls: C) -> C:
    """Transforms a class into a Singleton (only one instance can exist)."""

    @functools.wraps(cls)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if (
            not wrapper.instance
        ):  # type: ignore  # https://github.com/python/mypy/issues/2087
            wrapper.instance = cls(
                *args, **kwargs
            )  # type: ignore  # https://github.com/python/mypy/issues/2087
        return cast(
            C, wrapper.instance
        )  # type: ignore  # https://github.com/python/mypy/issues/2087

    wrapper.instance = (
        None
    )  # type: ignore  # https://github.com/python/mypy/issues/2087
    return cast(C, wrapper)


# This is mostly so that I practice decorators with optional parameters.
def repeat(
    _func: Optional[F] = None, *, num_times: int = 3
) -> Union[F, Callable[[F], F]]:
    """Repeats a function 3 times when decorated without arguments. Otherwise `num_times`."""

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(num_times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return cast(F, wrapper)

    if _func is None:
        return cast(F, decorator)
    return decorator(_func)


# This is mostly so that I practice using function attributes.
def count_calls(func: F) -> F:
    """Logs to DEBUG how many times a function gets called, saves the result in a newly created attribute `num_calls`."""
    _logger = logging.getLogger(__name__ + '.' + func.__name__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.num_calls += (
            1
        )  # type: ignore  # https://github.com/python/mypy/issues/2087

        _logger.debug(
            ' called %s times', wrapper.num_calls
        )  # type: ignore  # https://github.com/python/mypy/issues/2087
        return func(*args, **kwargs)

    wrapper.num_calls = 0  # type: ignore  # https://github.com/python/mypy/issues/2087

    return cast(F, wrapper)


# This is mostly so that I practice using a class as a decorator.
class CountCalls:
    """Logs to DEBUG how many times a function gets called, saves the result in a newly created attribute `num_calls`."""

    def __init__(self, func: F) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls: int = 0
        self._logger = logging.getLogger(__name__ + '.' + self.func.__name__)
        self.last_return_value = None

    __call__: F

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num_calls += 1
        self._logger.debug(' called %s times', self.num_calls)
        self.last_return_value = self.func(*args, **kwargs)
        return self.last_return_value
