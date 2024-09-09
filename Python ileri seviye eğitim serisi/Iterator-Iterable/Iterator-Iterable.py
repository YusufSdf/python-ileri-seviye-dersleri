

numbers = [1,2,3,4,5]

itrb = iter(numbers)
while True:
    try:
        number = next(itrb)
        print(number)
    except StopIteration:
        break
