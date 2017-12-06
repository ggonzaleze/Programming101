def max_number(x,y):
    if x >= y:
        return x
    else:
        return y
num1 =int(input("Please enter a number. "))
num2 =int(input("Please enter a second number. "))
print("The maximum number is ",max_number(num1,num2))
