def vowel(x):
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

character = input("Enter a single character. ")
character = character.upper()
print(vowel(character))
