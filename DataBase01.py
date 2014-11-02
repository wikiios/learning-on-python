#coding = utf-8
import anydbm
db = anydbm.open('captions.db', 'c')
db ['cleese.png'] = 'Photo of Jhon Cleese'
db['WR.jpg'] = 'Log of Microsoft'
print db['WR.jpg']
print db['cleese.png']
for k in db :
    print k
    
for key in db :
    print db[key]

db.close()
