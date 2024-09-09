def faktoriyel(number):
    def inner(number):
        if number <= 1:
            return 1
        return number * inner(number - 1)
    return inner(number)

result = faktoriyel(5)
print(result)