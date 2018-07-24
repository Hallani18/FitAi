# login system with a password
# the game assuming the username and password are correct
import sqlite3,time

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("fitai.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user, [(username), (password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[2])
            #return("exit")
            break
    
        else:
            print("Username and password not recognized")
            again = input("Do you want to try again? (y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return ("exit")
                break
login()
