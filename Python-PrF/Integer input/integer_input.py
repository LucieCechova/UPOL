x = int(input("Please enter an integer with atleast 3 digits : "))
if abs(x) > 100:
    x = str(x)
    print(f"Digit in the tens position is {x[-2]}")
else:
    print(f"Error: {x} has less than three digits")