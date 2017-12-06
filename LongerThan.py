def longer_than(n,words):
    longer = []
    for element in words:
        if len(element) > n:
            longer = longer + [element]
    return longer

list1 = ["hello","my","name","is","Gina"]
number = 3
print(longer_than(number,list1))
