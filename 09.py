import sys

try:
	s = raw_input('Enter something --> ')
except EOFError:#����EOFError���͵��쳣
	print '/nWhy did you do an EOF on me?'
	sys.exit() # �˳�����
except:#�����������쳣
	print '/nSome error/exception occurred.'
	
print 'Done'

try :
        float ([1,2])
except BaseException , da :
        pass
print type(da)
