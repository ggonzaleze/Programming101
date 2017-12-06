def char_freq(phrase):
    freq = {}
    for letter in phrase:
        freq[letter] = freq.get(letter,0) + 1
    return freq

phrase = "abbabcbdbabdbdbabababcbcbab"
print(char_freq(phrase))
