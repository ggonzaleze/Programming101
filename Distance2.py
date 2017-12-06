import math

def distance(A,B):
    return  math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

x1, y1 = [float(x) for x in input("Please enter the x and y values of the first point: ").split()]
x2, y2 = [float(x) for x in input("Please enter the x and y values of the second point: ").split()]
point1 = [x1,y1]
point2 = [x2,y2]
print("The distance between the points is: %0.2f" % distance(point1,point2))
