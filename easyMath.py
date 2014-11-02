#!/usr/bin/env python
from operator import add, sub
from random import randint, choice

ops = { '+' : add, '-' : sub }
M = 2
def d () :
    op = choice('+-')
    nums = [randint(1,100) for i in range(2)]
    nums.sort(reverse = True)
    a = ops[op] (*nums)
    pr = '%d %s %d = ' % (nums[0],op,nums[1])
    oops = 0
    while True :
        try :
            if int(raw_input(pr)) == a :
                print 'correct !'
                break
            if oops == M :
                print 'answer \n %s%d' %(pr,a)
            else :
                print 'incorrect ...... try again !\n'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError) :
            print 'invalid input ...... try again !\n'

def main() :
    while True :
        d()
        try :
            op = raw_input('Again? [y] \n').lower()
            if op and op[0] == 'n' :
                break
        except (KeyboardInterrupt, EOFError) :
            break
if __name__ == '__main__' :
    main()
