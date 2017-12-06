def correct(phrase):
    newstring = ""
    for i in range(len(phrase) - 1):
        if phrase[i] == " " and phrase[i+1] == " ":
            pass
        else:
            newstring += phrase[i]
        if phrase[i] == "." and phrase[i+1] != " ":
            newstring = newstring + " "
    return newstring

phrase = input("Please enter a phrase: ")
print(correct(phrase))
