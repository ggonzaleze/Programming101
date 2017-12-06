def translate(string):
    translation = ""
    for c in string:
        if c in ["a","e","i","o","u","A","E","I","O","U"," "]:
            translation = translation + c
        else:
            translation = translation + c + "o" + c
    return translation
phrase =input("Please enter a phrase. ")
print(translate(phrase))
