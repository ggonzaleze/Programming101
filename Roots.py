import math
def square_root(x):
    return math.sqrt(x)
def cube_root(x):
    return math.pow(x,1/3)
number = float(input("Please enter a number. "))
if number >= 0:
    S = square_root(number)
    C = cube_root(number)
    print("The square root of ",number," is ",S," and the cube root is ",C)
else:
    print("No negative roots.")
