def is_palindrome(word):
    reverse = word[::-1]
    return word == reverse

string =input("Please enter a word. ")
print(is_palindrome(string))
