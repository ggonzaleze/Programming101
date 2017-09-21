import string

def is_palindrome(text):
    text = text.replace(" ","")
    text = text.lower()
    punctuation = string.punctuation
    for character in text:
        for symbol in punctuation:
            if character == symbol:
                text = text.replace(character,"")
    reverse = text[::-1]
    return reverse == text

phrase =input("Please enter a phrase: ")
print(is_palindrome(phrase))
