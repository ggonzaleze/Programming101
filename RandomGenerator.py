import random
random = int(random.randint(0,100)) + 1
number=0
while random != number:
    number=int(input("Please try to guess the number!"))
    if number > random:
        print("Too high!")
    elif number < random:
        print("Too low!")
    else:
        print("You gave up!")
        break
else:
    print("You got it!")
