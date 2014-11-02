# -*- coing: UTF-8 -*-
def josephus(n,k):
    link=range(1,n+1) 
    ind=0
    for loop_i in range(n-1):
        ind = (ind+k)% len(link) 
        ind-=1
        print 'Kill:',link[ind]
        del link[ind]
        if ind==-1: # the last element of link
            ind=0
    print 'survice :',link[0]
   

if __name__ == '__main__':
    x,y=input('enter x,y:\n')
    if(x!=0 or y!=0):
        josephus(x,y)
        print '-'*30

#strip·½·¨
s = '123abc'
print s.strip('21')
a = '    def'
print a.strip()

#¾ØÕóÔËËã
A = []
B = []
A = input('ÊäÈëA¾ØÕó:')
B = input ('ÊäÈëB¾ØÕó')
def addm(A,B):
        h1 = len(A[0])
        h2 = len(B[0])
        s1 = len(A)/h1
        s2 = len(B)/h2
        if h1 == h2 and s1 == s2:
                for i in range(0,s1-1):
                        for j in range(0,h1-1):
                                A[i][j] = A[i][j] +B[i][j]
addm(A,B)
print A
