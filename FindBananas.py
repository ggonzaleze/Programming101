def find_bananas(phrase):
    times = 0
    phrase = phrase.lower()
    phrase = phrase.replace("*","")
    phrase = phrase.replace("banana","*")
    for c in phrase:
        if c == "*":
            times = times + 1
    return times

phrase = input("Please enter a phrase: ")
print("The word 'banana' appears ",find_bananas(phrase),"time(s).")
