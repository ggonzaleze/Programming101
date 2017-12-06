def min_of_four(numbers):
    return min(numbers)

numbers = [int(x) for x in input("Please enter four numbers separated by a space: ").split()]
print("The smallest number is: ",min_of_four(numbers))
