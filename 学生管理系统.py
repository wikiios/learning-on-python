import pickle
import struct
f = open('Stu.txt','w')
n = input('Please input the number of stus:')
s = struct.pack('i',n)
f.write(s)
s2 = 'Number    Name    High Level Maths    Lineral Math    Computer Introduction'
print len(s2)
f.write(s2)
i = 0
while i < n:
    num = input('Please input No.' + str(i+1) + 's number(11 bits):')
    name = input('Please input No.' + str(i+1) + 's name(3 words):')
    hlm = input('Please input No.' + str(i+1) + 's High level Maths:')
    lm = input('Please input No.' + str(i+1) + 's Lineral Math:')
    ci = input('Please input No.' + str(i+1) + 's CI:')
    s = int(num) + str(name)
    s = s + struct.pack('fff',hlm,lm,ci)
    f.write(s)
    i = i + 1
f.close()
