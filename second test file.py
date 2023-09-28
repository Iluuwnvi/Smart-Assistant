import sqlite3

#establish connection to a db
conn = sqlite3.connect('MFCC.db')

#create a cursor
c = conn.cursor()

#create a table once it is created just hash it out
'''
c.execute(""" CREATE TABLE customers (
        first_name text,
        last_name text,
        mfcc real
    )""")'''

c.execute("INSERT INTO MFCC VALUES('Benji', 'Emerton', '')" )

#commit our command to the datatbase
conn.commit()

#close the connection 
conn.close()