def is_member(x,a):
    for e in a:
        if e == x:
            return True
    return False
element = 3
all_elements = [1,2,3,4]
print(is_member(element,all_elements))
