def suma(x):
    sum_list = 0
    for element in x:
        sum_list = sum_list + element
    return sum_list
def multi(x):
    multi_list = 1
    for element in x:
        multi_list = multi_list * element
    return multi_list
x = [1,2,3,4]
y = suma(x)
z = multi(x)
print("The sum of the list is ",y," and the multiplication is ",z)
