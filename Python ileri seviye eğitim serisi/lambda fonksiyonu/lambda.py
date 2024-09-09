result = lambda x,y: x*y

print(result(2,5))


def my_func(n):
    return lambda x: x*n

result = my_func(10)

print(result(10))