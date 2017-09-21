def sum_squares(x,y,z):
    return x*x + y*y + z*z
def min_value(x,y,z):
    if x<=y<=z or x<=z<=y:
        return x
    elif y<=x<=z or y<=z<=x:
        return y
    else:
        return z
num1=int(input("Please enter a number."))
num2=int(input("Please enter a second number."))
num3=int(input("Please enter a third number."))
M=min_value(num1,num2,num3)
S=sum_squares(num1,num2,num3)
print("The minimum value is ", M ," and the sum of the squares is ", S)
