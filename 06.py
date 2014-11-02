import string
import math
import os
import sys
#zfill函数
c = '123'
string.zfill(c,30)

#divmod
divmod(33,4)

#Template函数
s = string.Template('there is a ${nima} called ${fuck}')
s.substitute(nima = 'baishu',fuck = 'chenjialong')
a = 20
b =30
print 
s.substitute(nima = a,fuck = b)

#coerce函数
print coerce(2.0,1+0j)

#金字塔输出
s = '12345'
for i in range(-1,-len(s),-1):
	print s[:i]

#字符串超灵活应用
quest = 'what is your favourite colour ?'
print quest.capitalize()
print quest.center(50)
print ':'.join(quest.split())

#堆栈管理
stack = []
def pushi():
        stack.append(raw_input('Enter New String: ').strip())

def popi():
        if len(stack) == 0:
                print 'cannot pop from an empty stack!'
        else:
                print 'Remove [',`stack.pop()`,']'
def views():
        print stack
CMDs = {'u' : pushi , 'o' : popi ,'v' :views}
def showmenu():
        pr = '''
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter your choice: '''
        while True:
                while True:
                        try:
                                choice = raw_input(pr).strip()[0].lower()
                        except  (EOFError,KeyboardInterrupt,IndexError):
                                choice = 'q'
                        print '\nYou picked : [%s] ' % choice
                        if  choice not in 'uvoq':
                                print 'Invalid option , try again'
                        else:
                                break
                if choice == 'q':
                        break
                CMDs[choice]()

if __name__ == '__main__':
        showmenu()

#队列queue
queue = []
def en():
        queue.append(raw_input('Enter New String: ').strip())
def de():
        if len(queue) == 0 :
                 print 'cannot pop from an empty queue!'
        else :
                print 'Removed [',`queue.pop(0)`,']'
def vi():
        print queue
CMD = {'e':en,'d':de,'v':vi}

def show():
        r = '''
(E)nQ
(D)eQ
(V)iew
(Q)uit

Enter your choice: '''
        while True:
                while True:
                        try:
                                choice = raw_input(r).strip()[0].lower()
                        except  (EOFError,KeyboardInterrupt,IndexError):
                                choice = 'q'
                        print '\nYou picked : [%s] ' % choice
                        if  choice not in 'edvq':
                                print 'Invalid option , try again'
                        else:
                                break
                if choice == 'q':
                        break
                CMD[choice]()

if __name__ == '__main__':
        show()
        
