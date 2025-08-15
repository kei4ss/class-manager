from Application.model.entities.Classroom import Classroom
from Application.model.dao.ClassroomDAO import ClassroomDAO


class ClassroomService:
    @staticmethod
    def insert(classroom:Classroom):
        if classroom.getName() and len(classroom.getName()) > 3 and classroom.getPrice() and classroom.getDayOfWeek():
            ClassroomDAO.insertClassroom(classroom)
            return True
        return False

    @staticmethod
    def getAll():
        return ClassroomDAO.getClassrooms()

    @staticmethod
    def getByName(name):
        try:
            result = ClassroomDAO.getClassroomByName(name)
        except Exception as e:
            print(e, " | Falha ao acessar banco de dados")
            result = None
        return result