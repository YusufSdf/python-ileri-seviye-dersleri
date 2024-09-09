import time
import threading

numbers = [2,5,8,25,22,15,9]
def square(numbers):
    for i in numbers:
        time.sleep(0.3)
        print("karesi: ",i*i)

def cube(numbers):
    for i in numbers:
        time.sleep(0.3)
        print("kübü: ",i*i*i)

t = time.time()

# square(numbers)
# cube(numbers)

th1 = threading.Thread(target=square,args=(numbers,)) # args yerinde tuple bekler virgül olmalı
th2 = threading.Thread(target=cube,args=(numbers,))

th1.start()
th2.start()

th1.join()# bekletiyor
th2.join()
print(time.time() - t)
