from src.repository.class_repository import ClassroomRepository

class ClassroomService:
    def __init__(self, session):
        self.classroomRepo = ClassroomRepository(session)
    
    def create(self, name:str):
        try:
            return self.classroomRepo.create(name)
        except:
            return False
    
    def get_all(self):
        try:
            return self.classroomRepo.get_all()
        except:
            return False