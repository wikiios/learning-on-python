import struct
f = open('Stu.txt','r')
s = f.read(4)
n= struct.unpack('i',s)
head = f.read(75)
print head + '     Average     '
i = 0
li = []
while i<n:
    i = i + 1
    s = f.read(11)
    num = s
    s = f.read(3)
    name = s
    s = f.read(12)
    hlm,lm,ci = struct.unpack('fff',s)
    a = (hlm + lm + ci) / 3
    li2=[num,name,hlm,lm,ci]
    li.append(li2)
i = 0
j = 0
while i < n :
    s2 = (li[i][0] + ' ' * 4)
    s2 = s2 +li[i][1] + ' ' * 4
    j = 2
    while j < 6:
        s = '%-13.2f'%li[i][j]
        j = j + 1
        s2 = s2 + s
    print(s2)
    i = i + 1
f.close()
