def list_lengths(words):
    numbers = []
    for element in words:
        numbers = numbers + [len(element)]
    return numbers

list1 = ["hello", "my","name","is","Gina"]
print(list_lengths(list1))
