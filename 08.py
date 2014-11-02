
#yield方法交叉配对样例2
rows = [3,17]
def cols():
        yield 56
        yield 2
        yield 1
r = ((i,j) for i in rows for j in cols())
for e in r :
        print e

#文件wri,''te
import os
f = open('h.txt','w+')
x = ['1\n','2\n','3\n','4\n','5\n','6\n']
#for e in x :
#        f.write(e+os.linesep)
f.writelines(x)
f.close()

#argv、argc参数查看
import sys
print 'you enter ', len(sys.argv), 'arguments'
print 'they are ' , str(sys.argv)

#os、os.path 模块示例：创建文本、写入数据、重命名、输出文件内容、遍历目录树、文件路径名操作
import os
for tmp in ('/tmp',r'c:\tmp') :
        if os.path.isdir(tmp):
                break
else :
        print 'no temp directory available'
        tmp = ''
if tmp :
        os.chdir(tmp)
        c = os.getcwd()
        print '***  current temporary directory  ***'
        print c

        print '***  creating example directionary  ***'
        os.mkdir('example')
        os.chdir('example')
        c = os.getcwd()
        print '***  new working directory  ***'
        print c
        print '***  original directory listing  ***'
        print os.listdir(c)

        print '***  creating test file  ***'
        f = open('test','w')
        f.write('f\n')
        f.write('u\n')
        f.write('c\n')
        f.write('k\n')
        f.close()
        print '***  updated directory listing  ***'
        print os.listdir(c)

        print "***  renaming 'test' to 'filetest.txt'"
        os.rename('test','filetest')
        print '***  updated directory listing  ***'
        print os.listdir(c)

        path = os.path.join(c,os.listdir(c)[0])
        print '***  full file pathname  ***'
        print path
        print '***  (pathname,basename) ==  ***'
        print os.path.split(path)
        print '***  (filename,extension) ==  ***'
        print os.path.splitext(os.path.basename(path))

        print '***  displaying file contents  ***'
        f = open(path)
        for e in f :
                print e
        f.close()

        print '***  deleting test file  ***'
        os.remove(path)
        print '***  updated directory listing  ***'
        print os.listdir(c)
        os.chdir(os.pardir)
        print '***  deleting test directory  ***'
        os.rmdir('example')
        print '***  done  ***'
