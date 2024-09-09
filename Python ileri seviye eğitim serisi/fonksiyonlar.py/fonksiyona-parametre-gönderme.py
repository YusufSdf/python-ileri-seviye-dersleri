def filter(fn, liste):
    result = []
    for item in liste:
        if fn(item) is True:
            result.append(item)
    return result


def is_even(num):
    return num % 2 == 0

def is_possitive(num):
    return  num > 0

numbers = [1,2,3,-5,-6,-7,50,55,100]

sonuc = filter(is_even,numbers)
sonuc = filter(is_possitive,numbers)

print(sonuc)

