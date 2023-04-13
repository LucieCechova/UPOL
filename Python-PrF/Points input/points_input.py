coords = input("Please enter points:")
coords_squared = []
coords = coords.split(";")
for pair in coords:
    x, y = pair.split(",")
    x, y = float(x), float(y)
    x_squared, y_squared = x ** 2, y ** 2
    point = {"x": x_squared, "y": y_squared}
    coords_squared.append(point)
print(coords_squared)
