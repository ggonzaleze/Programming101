#This program calculates the square root of a number using the Babylonian method
def babylonian_method(x):
    initial_guess = x/2
    difference = 1
    while difference > 0.0001:
        guess = .5 * (initial_guess + x/initial_guess)
        difference = initial_guess - guess
        initial_guess = guess
    return guess

x = float(input("Please enter a number: "))
print("The approximate square root of the number is: %0.4f" % babylonian_method(x))
