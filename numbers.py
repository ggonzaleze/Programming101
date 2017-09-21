def numbers_sum(x,y):
    addition = x + y
    return addition
def number_subs(x,y):
    substraction = x - y
    return substraction
def number_multi(x,y):
    multiplication = x * y
    return multiplication
def number_div(x,y):
    if y == 0:
        division = "Mathematical error."
    else:
        division = x // y
    return division
def number_rem(x,y):
    if y == 0:
        remainder = "Mathematical error."
    else:
        remainder = x % y
    return remainder
num1=int(input("Please enter a number. "))
num2=int(input("Please enter a second number. "))
print("The sum of these numbers is: ",numbers_sum(num1,num2))
print("The substraction of these numbers is: ",number_subs(num1,num2))
print("The multiplication of these numbers is: ",number_multi(num1,num2))
print("The division with no decimals of these numbers is: ",number_div(num1,num2))
print("The remainder of the division of these numbers is: ",number_rem(num1,num2))
