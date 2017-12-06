def semordnilap_recogniser(File):
    open_file = open(File,'r')
    lines = open_file.readlines()
    lines = [element.strip() for element in lines]
    lines = [element.lower() for element in lines]
    reverse = ""
    semordnilaps = []
    for element in lines:
        reverse = element[::-1]
        if reverse in lines:
            if reverse not in semordnilaps:
                semordnilaps = semordnilaps + [reverse] + [element]
    open_file.close()
    return semordnilaps

path = input("Please enter the file: ")
print("Found this semordnilaps: ",semordnilap_recogniser(path))
