# -*- coding: UTF-8 -*-
#双序列同时对应迭代
num  = [1998,2000,1995,2013]
name = ['a','b','c','d']
for y, n in zip(num,name):
    print y, n

#else 配合while
c = input('input a number: ')
d = c
c /=2
while c > 1 :
    if d % c == 0:
        print 'largest factor of %d is %d' % \
              (d,c)
        break
    c -= 1
else: print '%d is a primer' % d

#迭代器
t = (123,'s',1.0,1+1j)
i = iter(t)
print i.next()
print i.next()

#字典+迭代器
di = {('Paul','author'):('1995','18'),
      ('Jobs','engineer'):('1994','19'),
      ('Nick','teacher'):('1996','17')
    }
for each in di :
    print 'Name : %s pro : %s' % each
    print 'bitrh year : %s  age : %s' % di[each]
