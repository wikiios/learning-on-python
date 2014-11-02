#×¥È¡webÒ³Ãæ
from urllib import urlretrieve
import re
'''
def fi (lines) :
    for e in lines :
        if not e.strip() :
            continue
        else :
            return e[0:20]

def fl(webpage) :
    f = open (webpage)
    lines = f.readlines()
    f.close()
    print fi(lines),'\n'
    lines.reverse()
    print fi(lines)
'''
def fi (lines) :
    key = 'jpg'
    for e in lines :
        k = re.search(key, e)
        if not e.strip() :
            continue
        elif  k:
            return k.groups()
        else :
            break

def dl (url = 'http://www.baidu.com/', process = fi) :
    try :
        r = urlretrieve(url)[0]
    except IOError :
        r = None
    if r :
        process(r)
if __name__ == '__main__':
    dl()
