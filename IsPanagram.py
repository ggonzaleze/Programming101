def is_panagram(sentence):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sentence = sentence.lower()
    letters = []
    for character in sentence:
        letters = letters + [character]
    match = set(alphabet) & set(letters)
    match_list = []
    for element in match:
        match_list = match_list + [element]
    common = len(match_list)
    if common == 26:
        return True
    return False

sentence = input("Please enter a phrase: ")
print(is_panagram(sentence))
