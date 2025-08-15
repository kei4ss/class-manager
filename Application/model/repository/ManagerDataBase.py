import sqlite3
import pathlib
import os

class ManagerDataBase:
    parentPath = pathlib.Path(__file__).parent
    databasePath = parentPath / 'database.db'

    database = None
    cursor = None

    @staticmethod
    def getClassrooms():
        sql = "SELECT * FROM classroom"
        result = ManagerDataBase.cursor.execute(sql)
        return result.fetchall()

    @staticmethod
    def restartDatabase():
        ManagerDataBase.deleteDatabase()
        ManagerDataBase.initializeDatabase()

    @staticmethod
    def initializeDatabase():
        ManagerDataBase.database = sqlite3.connect(ManagerDataBase.databasePath)
        ManagerDataBase.cursor = ManagerDataBase.database.cursor()
        sql = "CREATE TABLE IF NOT EXISTS classroom( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, price INTEGER NOT NULL,dayOfWeek TEXT NOT NULL);"
        ManagerDataBase.cursor.execute(sql)
        ManagerDataBase.database.commit()



    @staticmethod
    def deleteDatabase():
        try:
            ManagerDataBase.database.close()
            os.remove(ManagerDataBase.databasePath)
        except Exception as e:
            print(e)


