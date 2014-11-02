#!/usr/bin/env python
from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial (Tkinter.Button, root, fg = 'white', bg = 'blue')
b1 = MyButton (text = 'hello world')
b2 = MyButton (text = 'goodbye')
qb = MyButton (text = 'QUIT', bg = 'brown', command = root.quit)
b1.pack()
b2.pack()
qb.pack (fill = Tkinter.X, expand = True)
root.title ('Fuck you !')
root.mainloop()

#
