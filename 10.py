#信用卡交易系统
#!/usr/bin/env python
def safe_float(obj) :
    'safe version of float()'
    try :
        retval = float(obj)
    except (ValueError , TypeError ), diag :
        retval = str(diag)
        return retval

def main() :
    'handles all the data processing'
    log = open('cardlog.txt','w')
    try :
            ccfile = open('carddata.txt','r')
            txns = ccfile.readlines()
    except IOError :
            log.write('no txns this month \n')
    
    total = 0.0
    log.write('account log :\n')

    for eachtxn in txns :
        result = safe_float(eachtxn)
        if isinstance(result, float) :
              total += result
              log.write('data... processed\n')
        else :
            log.write('ignore: %s'%result)
    print '$%.2f (new balance)'%(total)
    ccfile.close()
    log.close()
if __name__ == '__main__' :
    main()
