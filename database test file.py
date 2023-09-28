import sqlite3
conn = sqlite3.connect('MFCC.db')#establish connection to a db
c = conn.cursor()#create a cursor
c.execute('SELECT mfcc FROM people')
tbldata = c.fetchall()
print(tbldata)
for row in tbldata:
    print(row)