from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def read_points(text, separator=";"):
    """Separating string of points to list of named coordinates."""
    coords = text.split(separator)
    output = []
    for pair in coords:
        x, y = pair.split(",")
        point = Point(float(x), float(y))
        output.append(point)
    return output
