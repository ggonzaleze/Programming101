def generate_n_chars(n,c):
    n = int(n)
    answer = ""
    while n != 0:
        answer = answer + c 
        n = n - 1
    return answer
number = input("Please introduce an integer. ")
character = input("Please introduce a single character. ")
print(generate_n_chars(number,character))
