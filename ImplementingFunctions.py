def implement_map(function,elements):
    return [function(x) for x in elements]

def implement_filter(function,elements):
    true = []
    for x in elements:
        if function(x) == True:
            true = true + [x]
    return true

def implement_reduce(function,elements):
    result = elements[0]
    i = 1
    if len(elements) > 1:
        for x in elements[1:]:
            result = function(result,elements[i])
            i = i + 1
    return result

numbers = [1,2,3,4]
print(implement_map(lambda x : x**2, numbers)) #answer: [1,2,9,16]
print(implement_filter(lambda x : x % 2 == 0,numbers)) #answer: [2,4]
print(implement_reduce(lambda x,y : x * y,numbers)) #answer: 24
