db  = {}
def newuser() :
    p = 'login desired: '
    while True:
        name = raw_input(p)
        if db.has_key(name) :
            p = 'name has been taken , try another: '
            continue
        else :
            break
    pwd = raw_input('New password: ')
    pwd2 = raw_input('Confirm new password: ')
    while pwd != pwd2 :
        pwd2 = raw_input('Confirm new password: ')
    else :
        pass
    db[name] = pwd

def olduser() :
    name = raw_input('login: ')
    pwd = raw_input('password: ')
    password = db[name]
    if password == pwd :
        print 'Login success !'
        print 'Welcome back' , name
    else :
        print 'Login Error'

def showmenu():
    p = '''
(N)ew User Join
(O)ld User Login
(Q)uit

Enter choice:'''

    done = False

    while not done :
        try :
                choice = raw_input(p).strip()[0].lower()
        except (EOFError ,KeyboardInterrupt) :
                choice = 'q'
        print '\n You picked : [%s]'%choice
        if choice not in 'noq' :
            print 'invalid option , try again '
        else :
            chosen = True
        if choice == 'q' :
            done = True
        if choice == 'n' :
            newuser()
        if choice == 'o' :
            olduser()
if __name__ == '__main__' :
    showmenu()

