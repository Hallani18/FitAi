import sqlite3
conn=sqlite3.connect("fitai.db")
cursor=conn.cursor()

def tbcreatepeople():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
            people( 
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) NOT NULL,
            firstname VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
           password VARCHAR(20) NOT NULL,
           email VARCHAR(40) NOT NULL,
           UNIQUE(userID)
           UNIQUE(username)
           )''')
        conn.commit()
        print('Table Created Successfully')
    except Error as e:
        print(e)
def insertadminintopeople():
    try:
        cursor.execute('''INSERT INTO people(username, firstname, surname, password, email)
                   Values( 'Administrator', 'Ad', 'Min', 'abc', 'administrator@email.com')''')
        conn.commit()
        print('Admin Account Created Successfully')
    except Error as e:
        print(e)
def tbcreateinformation():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
            information( 
            userID INTEGER,
            gender INTEGER(1) NOT NULL,
            age VARCHAR(20) NOT NULL,
            height VARCHAR(20) NOT NULL,
            weight VARCHAR(20) NOT NULL,
           goal VARCHAR(20) NOT NULL,
           UNIQUE(userID)
           FOREIGN KEY(userID) REFERENCES people(userID)
           )''')
        conn.commit()
        print('Table Created Successfully')
    except Error as e:
        print(e)

    
tbcreatepeople()
insertadminintopeople()
tbcreateinformation()
conn.close()
