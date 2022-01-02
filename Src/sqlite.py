from os import close
import sqlite3



def createTable():
    database = sqlite3.connect('readings.db')
    database.execute('''CREATE TABLE FARM
         (ID INT PRIMARY KEY     NOT NULL,
         TAGNUMBER           CHAR(10)    NOT NULL,
         AVERAGETEMP            INT     NOT NULL,
         DATETIME              TEXT    NOT NULL)
    
    ''')
    database.close()

def getNextID():
    database = sqlite3.connect('readings.db')
    cursor = database.execute("""SELECT * FROM FARM""")
    result = cursor.fetchall();
    id = len(result)+1
    database.close()
    print(int(id))    
    return int(id)

def addToDatabase(ID,TAGNUMBER,AVERAGETEMP,DATE):
    database = sqlite3.connect('readings.db')
    database.execute("INSERT INTO FARM (ID,TAGNUMBER,AVERAGETEMP,DATETIME) \
        VALUES(?,?,?,?)",(ID,TAGNUMBER,AVERAGETEMP,DATE))
    database.commit()
    database.close()