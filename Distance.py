import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input("Please introduce the x value of the first point: "))
y1 = float(input("Please introduce the y value of the first point: "))
x2 = float(input("Please introduce the x value of the second point: "))
y2 = float(input("Please introduce the y value of the second point: "))
print("The distance between the points is %0.2f" % distance(x1,y1,x2,y2))
