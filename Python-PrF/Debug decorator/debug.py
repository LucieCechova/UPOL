import functools


def debug(func):
    "Prints name of function, her arguments and result."

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arguments_list = []
        kwarguments_list = []

        for arg in args:
            arguments_list.append(repr(arg))

        for kwarg_name, kwarg_value in kwargs.items():
            kwarguments_list.append(f"{kwarg_name}={kwarg_value}")

        arg_kwarg_list = arguments_list + kwarguments_list
        arg_kwarg = ", ".join(arg_kwarg_list)

        print(f"Calling: {func.__name__}({arg_kwarg})")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper
