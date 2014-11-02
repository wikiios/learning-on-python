import sys

try:
	s = raw_input('Enter something --> ')
except EOFError:#处理EOFError类型的异常
	print '/nWhy did you do an EOF on me?'
	sys.exit() # 退出程序
except:#处理其它的异常
	print '/nSome error/exception occurred.'
	
print 'Done'

try :
        float ([1,2])
except BaseException , da :
        pass
print type(da)
