#filter 方法
from random import randint
a = []
def odd( n ) :
    return n%2
for i in range(10):
    a.append(randint(1,100))
print filter(odd, a)

#reduce 方法

#map 方法
s1 = [1, 3, 5, 7, 9]
s2 = [2, 4, 6, 8, 0]
s3 = [10, 100, 1000, 10000]
print map(lambda x, y: (x+y,x+y), s1, s2)

#reduce 方法
print reduce(lambda x, y : x + y ,range(10))
print reduce(lambda x, y : x + y, [1, 4, 10, 100])

#partial
from functools import partial
baseTwo = partial (int ,base = 2)
s = raw_input()
print baseTwo(s)
base16 = partial(int, base = 16)
print base16(s)

#函数取代字典
def test(par):
    print par

def test1():
    print 1000

def f(x):
    return {
        'a': test,
        'b': test1,
        }.get(x, test)

print f('a')(100)
print f('b')()

#apply函数应用
def x(*t) :
    for i in t :
        print i
apply(x, (1, 2, 3, 4))

#变量作用范围
def foo():
    m = 4   
    def bar():
        n = 4
        print m + n
    print m
    bar()
foo()


