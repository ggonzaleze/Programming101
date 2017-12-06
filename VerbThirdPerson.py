def make_3sg_form(verb):
    verb = verb.lower()
    if verb.endswith("y"):
        verb = verb.replace("y","ie")
    else:
        endings = ["o","ch","s","sh","x","z"]
        for element in endings:
            if verb.endswith(element):
                verb = verb + "e"
                break
    verb = verb + "s"
    return verb

verb = input("Please enter a verb in infinitive: ")
print("The third person of the verb is: ",make_3sg_form(verb))
