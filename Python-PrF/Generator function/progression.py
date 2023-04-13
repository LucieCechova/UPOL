def arithmetic_progression(begin, step, end=None):
    """Returns numbers in arithmetic progression."""
    while not end or begin < end:
        yield begin
        begin += step
