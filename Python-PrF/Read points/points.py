def read_points(text, separator=";"):
    """Separating string of points to list of named coordinates."""
    coords = text.split(separator)
    output = []
    for pair in coords:
        x, y = pair.split(",")
        x, y = float(x), float(y)
        point = {"x": x, "y": y}
        output.append(point)
    return(output)
