def max_length(words):
    maximum = 0
    word = ""
    for element in words:
        length = len(element)
        if length > maximum:
            maximum = length
            word = element
    return word,maximum

list1 = ["hello","my","name","is","Gina"]
print("The longest word and its length, respectively, are ",max_length(list1))
