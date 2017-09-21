def files_count(text):
    lines = 0
    characters = 0
    text_file = open(text,'r')
    read = text_file.readlines()
    for element in read:
        element = element.strip()
        lines = lines + 1
        for c in element:
            characters = characters + 1
    text_file.close()
    return (lines,characters)

path = 'C:/Users/georg/Documents/python/week.txt'
print("The number of lines and characters, respectively, is: ",files_count(path))
