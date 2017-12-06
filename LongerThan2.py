def filter_long_words(words,n):
    return list(filter(lambda x : len(x) > n, words))

words = ["Hello","my","name","is","Gina"]
n = 2
print("The words longer than ",n," are ",filter_long_words(words,n))
