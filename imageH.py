from PIL import Image
import os
filelist = os.listdir('C:/Users/���/Pictures/IMAGE')+[]
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+'jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print 'Cannot convert',infile
#ת��Ŀ¼��ͼƬΪjpg��ʽ
