def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def calculate_e(precision):
    initial_guess = 1
    difference = 10
    e = 2
    x = 2
    while difference > precision :
        e = e + 1 / factorial(x)
        difference = e - initial_guess
        initial_guess = e
        x = x + 1
    return e

precision = float(input("Introduce the precision you want: "))
print(calculate_e(precision))
