coords = input("Please enter an point where x and y coordinates are separated by comma (i.e. 20,-10.23):")
comma = coords.index(",")
x = float(coords[:comma])
y = float(coords[comma+1:])
x_squared, y_squared = x ** 2, y ** 2
print(f"x^2: {x_squared}, y^2: {y_squared}")