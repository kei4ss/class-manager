from Application.model.entities.Classroom import Classroom
from Application.model.repository.ManagerDataBase import ManagerDataBase


class ClassroomDAO:

    @staticmethod
    def insertClassroom(classroom:Classroom):
        name = classroom.getName()
        price = classroom.getPrice()
        dayOfWeek = classroom.getDayOfWeek().name

        sql = "INSERT INTO classroom (name, price, dayOfWeek) VALUES (?, ?, ?)"
        ManagerDataBase.cursor.execute(sql, (name, price, dayOfWeek))
        ManagerDataBase.database.commit()

    @staticmethod
    def getClassrooms():
        sql = "SELECT * FROM classroom"
        result = ManagerDataBase.cursor.execute(sql)
        return result.fetchall()

    @staticmethod
    def getClassroomByName(name):
        sql = "SELECT * FROM classroom WHERE name = ?"
        result = ManagerDataBase.cursor.execute(sql, (name,))
        return result.fetchall()