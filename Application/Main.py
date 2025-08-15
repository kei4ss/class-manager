from Application.model.dao.ClassroomDAO import ClassroomDAO
from Application.model.repository.ManagerDataBase import ManagerDataBase
from Application.model.service.ClassroomService import ClassroomService
from Application.screen.MainScreen import MainScreen

def main():
    ManagerDataBase.initializeDatabase()
    MainScreen().main()
    #ManagerDataBase.deleteDatabase()

if __name__ == '__main__':
    main()
