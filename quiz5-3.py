def lenght(string):
    letters = 0
    for c in string:
        letters = letters + 1
    return letters
phrase = input("Please enter a phrase. ")
print("The lenght of the phrase is ",lenght(phrase)," characters.")
