import sqlite3
conn=sqlite3.connect("fitai.db")
cursor=conn.cursor()

def tbcreatepeople():
    try:
        cursor.execute('''INSERT
            people( 
            userID INTEGER PRIMARY KEY,
            username VARCHAR(20) NOT NULL,
            firstname VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
           password VARCHAR(20) NOT NULL
           )''')
        conn.commit()
        conn.close()
        print('Table Created Successfully')
    except Error as e:
        print(e)


    
tbcreatepeople()
