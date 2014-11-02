# -*- coding: UTF-8 -*-
import os
import string
#迭代器
items = ['C','S','P']
for item in items:
    print item,
for item in items:
    print item

#装饰器
import time


def T(func):
    def wrapper():
        start = time.clock()
        func();
        end = time.clock()
        print end - start
    return wrapper

@T
def foo():
    print 'in foo()'

foo()

#列表的队列
from collections import deque
l = [1,2,'3',4.0]
print l
l2 = deque([5,6.0,7,'8'])
print l2
l2.popleft()
print l2

import os
#异常处理
try:
    f = open('file.txt')
except IOError,e:
        print e
else:
        print 'wrong'


#默认参数
def foo(debug = True):
    'determine if in debug mode with default argument'
    if debug:
        print 'in debug mode'
    print 'done'
foo(True)
foo(False)

#对象调用次数函数方法
import sys
sys.getrefcount('a')



#类的定义
class Fooclass(object):
    """My original class:Fooclass"""
    __version__ = 0.1

print Fooclass.__version__
print Fooclass.__name__

#lamba 表达式
def Times(n):
    return lambda s:s*n
twice = Times(2)
print twice(5)
print twice('Hello world')
