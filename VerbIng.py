def make_ing_form(verb):
    verb = verb.lower()
    if verb.endswith("ie"):
        verb = verb.replace("ie","y")
    elif verb.endswith("e"):
        if not verb.endswith("ee"):
            verb = verb.replace("e","")
    else:
        vowels = ["a","e","i","o","u"]
        if verb[-1] not in vowels:
            if verb[-2] in vowels:
                if verb[-3] not in vowels:
                    verb = verb + verb[-1]
    verb = verb + "ing"
    return verb

verb = input("Please introduce a verb: ")
print("The present participle of the verb is: ",make_ing_form(verb))
