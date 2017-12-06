def find_lycherels(x,y):
    nat_palin = 0
    palin = 0
    lycherel = 0
    for n in range(x,y+1):
        times = 0
        n = str(n)
        reverse = n[::-1]
        if reverse == n:
            nat_palin = nat_palin + 1
        else:
            copy_number = n
            while times < 30 and copy_number != reverse:
                copy_number = (int(copy_number)) + (int(reverse))
                copy_number = str(copy_number)
                reverse = copy_number[::-1]
                times = times + 1
            if copy_number == reverse:
                palin = palin + 1
            else:
                lycherel = lycherel + 1
                print("Found a lycherel: ",n)
    return nat_palin,palin,lycherel

lowest =int(input("Please enter the lowest value: "))
highest =int(input("Please entere the highest value: "))
print("The number of natural palindromes, non-lycherels, and lycherels is:",find_lycherels(lowest,highest))
