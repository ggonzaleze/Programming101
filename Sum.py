print("This program gives you the sum of a range of values.")
numero = int(input("Please enter the lowest number. "))
numero2 = int(input("Please enter the highest number. "))
if numero <= numero2:
    suma=0
    while (numero != (numero2 + 1)):
        suma = suma + numero
        numero = numero + 1
else:
    print("You need to enter your lowest value first.")
    suma="invalid."
print("The sum is ",suma)
