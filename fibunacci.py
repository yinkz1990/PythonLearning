from time import time


def fib(number):
    list = [0, 1]
    a = time()
    while len(list) <= number:
        new = list[-1] + list[-2]
        list.append(new)
    print(time() - a)

    return list


fib(10000)


def fib2(number):
    a = 0
    b = 1
    c = time()
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + a
    print(time() - c)


list_1 = []
for x in fib2(10000):
    list_1.append(x)
