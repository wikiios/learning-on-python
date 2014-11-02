#函数装饰器
from time import ctime, sleep

def T (func):
    def wrap():
        print '[%s] %s called '% (ctime(), func.__name__)
        return func()
    return wrap

@T
def f():
    pass

f()
sleep(4)

for i in range(3):
    sleep(1)
    f()

#传递调用函数

def c(func, seq) :
    'convert sequence of numbers to same type'
    return [func(each) for each in seq]

myseq = [123, 45.67, -6.2e8, 99999999L]
print c(int, myseq)
print c(float, myseq)
print c(long, myseq)
