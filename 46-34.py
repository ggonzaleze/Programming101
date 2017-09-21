def char_freq_table(File):
    open_file = open(File,'r')
    content = open_file.read()
    content = content.strip()
    chars = {}
    for c in content:
        chars[c] = chars.get(c,0) + 1
    return chars

path = 'C:/Users/georg/Documents/python/words.txt'
print(char_freq_table(path))
