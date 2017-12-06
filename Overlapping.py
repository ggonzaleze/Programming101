def overlapping(a,b):
    for c in a:
        for e in b:
            if c == e:
                return True
    return False
list1 =[1,2,3,4]
list2 =[8,5,6]
print(overlapping(list1,list2))
