from src.model.classroomModel import Classroom

class ClassroomRepository:
    def __init__(self, session):
        self.session = session
    
    def create(self, name:str):
        classroom = Classroom(name = name)
        self.session.add(classroom)
        self.session.commit()
        return classroom

    def get_all(self):
        return self.session.query(Classroom).all()

