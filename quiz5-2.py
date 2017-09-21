def max_number(x,y,z):
    if x >= y >= z or x >= z >= y:
        return x
    elif y >= x >= z or y >= z >= x:
        return y
    else:
        return z
num1 =int(input("Please enter a number. "))
num2 =int(input("Please enter a second number. "))
num3 =int(input("Please enter a third number. "))
print("The maximum number is ",max_number(num1,num2,num3))
