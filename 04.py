# -*- coding: UTF-8 -*-
#class method和文档
class FOO:
    pass
foo = FOO
print type(FOO)
print type(foo)
class x:
    '''hello ,this is my class'''
    def __init__(self,name):
        self.name = name
    def usa(self):
        print 'usa',self.name
y = x('fuck')
y.__init__
y.usa()


#super()方法：多重继承
class A:
    def  __init__(self):
      print "enter A"
      print "leave A"

 class B:
     def  __init__(self):
         print "enter B"
         print "leave B"

 class C(A):
     def __init__(self):
         print "enter C"
         super(C, self).__init__()
         print "leave C"

 class D(A):
     def __init__(self):
         print "enter D"
         super(D, self).__init__()
         print "leave D"
 class E(B, C):
     def __init__(self):
         print "enter E"
         B.__init__(self)
         C.__init__(self)
         print "leave E"

 class F(E, D):
     def __init__(self):
         print "enter F"
         E.__init__(self)
         D.__init__(self)
         print "leave F"

f=F
