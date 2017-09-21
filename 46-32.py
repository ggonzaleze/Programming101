import string

path = input("Please introduce the path of the file: ")
open_file = open(path,'r')
lines = open_file.readlines()
punctuation = string.punctuation
reverse = ""
palindromes = 0
for line in lines:
    for character in line:
        for symbol in punctuation:
            if character == symbol:
                line = line.replace(character,"")
    line = line.strip()
    line = line.replace(" ","")
    line = line.lower()
    reverse = line[::-1]
    if reverse == line:
        print("Found a palindrome!: ",line)
        palindromes = palindromes + 1
open_file.close()
print("Total: ",palindromes," palindromes.")
