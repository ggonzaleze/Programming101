def stan_dev(elements):
    step1 = sum(elements) / len(elements)
    step2 = sum((number - step1)**2 for number in elements)
    step3 = step2 / len(elements)
    step4 = step3**.5
    return step4
num1,num2,num3,num4,num5,num6,num7,num8,num9,num10 = [float(x) for x in input("Please enter 10 numbers separated by a space ").split()]
list1 = [num1, num2 , num3 , num4 , num5 , num6 , num7 , num8 , num9 , num10]
print("The total of those numbers is ",sum(list1))
print("The average of those numbers is ",sum(list1) / len(list1))
print("The standard deviation of those numbers is ",stan_dev(list1))
