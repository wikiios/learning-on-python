# -*- coding:UTF-8 -*-
#文件
f = file('txt.txt','r')
x = f.readlines()
for each in x:
        print each
f.close()

#生成器表达式
data = file('sample.txt','r')
a = len([word for line in data for word in line.split()])
print a
import os
print os.stat('sample.txt').st_size
b = sum(len(word) for line in data for word in line.split())
print b

#yield方法交叉配对样例
rows = [1,2,3,17]
def cols():
        yield 56
        yield 2
        yield 1
r = ((i,j) for i in rows for j in cols())
for e in r :
        print e

#以类实现的迭代器
class Fab(object):
        def __init__(self,max):
                self.max = max
                self.n, self.a, self.b = 0, 0, 1

        def __iter__(self):
                return self

        def next(self):
                if self.n < self.max :
                        r = self.b
                        self.a, self.b = self.b, self.a + self.b
                        self.n = self.n + 1
                        return r
                raise StopIteration()

#yield方法实现迭代
def fab(max):
        n, a, b = 0, 0, 1
        while n < max :
                yield b
                #print b
                a , b = b, a + b
                n = n + 1
for n in fab(10):
        print n

#最精简方法实现字符串最大长度显示
print max(len(x.strip()) for x in open('txt2.txt','r'))

#异常处理
def foo(a) :
        try:
                float (a)
        except ValueError :
                print 'could not convert non-number o float'
        except TypeError :
                print 'object typr cannot be converted to float'
        else :
                print 'correct'
foo('heloo')
foo([1,2])
foo(1.20)

def foo2():
        raise Exception('throw out a exception')
foo2()
