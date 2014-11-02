from PIL import Image
import os
filelist = os.listdir('C:/Users/青帝/Pictures/IMAGE')+[]
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+'jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print 'Cannot convert',infile
#转化目录下图片为jpg格式
