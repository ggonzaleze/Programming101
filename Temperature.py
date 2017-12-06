def Celsius(x):
    return 5*(x-32)/9
print("This program converts temperature from Fahrenheit to Celsius.")
F=int(input("Please enter the Fahrenheit temperature."))
C=Celsius(F)
print ("The temperature in Celsius is ",C)
if C<100:
    print("The water won´t boil at this temperature.")
else:
    print("The water will boil at this temperature.")
