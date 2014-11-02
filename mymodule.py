#!/usr/bin/python
#Filename:mymodule.py
'''hello this is my module'''

def sayh():
    print('Hello,this is my module speaking\n')

__version__ = '0.1'
#End of mymodule.py

def which():
    if __name__ == '__main__':
        print('Running by itself')
    else:
        print('Having been imported from anothoer module')
