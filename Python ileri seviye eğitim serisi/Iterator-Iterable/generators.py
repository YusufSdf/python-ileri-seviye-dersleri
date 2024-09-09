def counter(max):
    number = 1
    while number <= max:
        yield number
        number += 1

generator = counter(20)
# print(list(generator))

for i in generator:
    print(i)