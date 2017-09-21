from functools import reduce
n = int(input("Enter the number you want the factorial of: "))
factorial = reduce((lambda x, y : x * y), range(1,n + 1))
print("The factorial of ",n," is ",factorial)
