import time
import functools


def delay(seconds=1):
    "Delays program by x seconds"

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator
