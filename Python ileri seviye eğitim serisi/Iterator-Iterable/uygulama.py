# def counter():
#     number =0
#     while True:
#         yield number **2
#         number += 1
        
# g = counter()       

# for i in g:
#     print(i)


def fibo(max):
    a,b = 0,1
    count = 0
    while count <= max:
        a,b = b, a+b
        yield b
        count += 1


g = fibo(10)
for i in g:
    print(i)
