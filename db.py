from secret import *

class Mydb:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    def connect(self):
        connection=mysql.connector.connect(host=self.host,user=self.user,password=self.password,
        database=self.database)
        return connection

