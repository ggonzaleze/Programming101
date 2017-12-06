def factorial(x):
    if x < 0:
        return "sorry, that is not a positive number!"
    elif x == 0:
        return 1
    else:
        recurse = factorial(x-1)
        result = x * recurse
        return result

again = "YES"
while again != "NO":
    n = int(input("Please enter a positive number: "))
    print("The factorial of the number is: ",factorial(n))
    again = input("Would you like to try again? ")
    again = again.upper()
print("Have a nice day!")
