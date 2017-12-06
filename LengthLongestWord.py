from functools import reduce

def find_longest_word(words):
    lengths = list(map(lambda x : len(x), words))
    return reduce(lambda x,y : x if x > y or x == y else y, lengths)

words = ["Hello","my","name","is","Gina"]
print("The length of the longest word is: ",find_longest_word(words))
