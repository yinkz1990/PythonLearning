from time import time


def function1(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} m')
        return result
    return wrap_func


@function1
def testing():
    for i in range(100000000):
        i*5


testing()
