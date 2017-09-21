from functools import reduce

def max_in_list(numbers):
    return reduce(lambda x,y : x if x > y or x == y else y , numbers)

numbers = [-5,10,6,0]
print("The maximum number is: ",max_in_list(numbers))
