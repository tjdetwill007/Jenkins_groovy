from db import *
def dbfun(usr_email,usr_password):
    dbCred=get_secret()
    dbInstance=Mydb(dbCred["host"],dbCred["username"],dbCred["password"],dbCred["dbname"])
    try:
        a=dbInstance.connect()
        print (a)
        mycursor=a.cursor()
        mycursor.execute(f"SELECT * FROM accounts WHERE email= \"{usr_email}\" AND password = \"{usr_password}\"")
        myresult = list(mycursor.fetchone())
        # return myresult
        # print(myresult)
        row = dict(zip(list(mycursor.column_names),myresult)) #using Zip to merge two list as dict.
        return row
    except Exception as e:
        print (e)

def dbcreate(username,password,email):
    try:

        dbCred=get_secret()
        dbInstance=Mydb(dbCred["host"],dbCred["username"],dbCred["password"],dbCred["dbname"])
        dbInstance=dbInstance.connect()
        mycursor = dbInstance.cursor()

        sql = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
        val = (username,password,email)
        mycursor.execute(sql, val)

        dbInstance.commit()

    except Exception as e:
        print(e)
        return 0       