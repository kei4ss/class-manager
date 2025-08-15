from Application.model.entities.Classroom import Classroom
from Application.model.entities.DayWeek import DayWeek
from Application.model.service.ClassroomService import ClassroomService
from Application.model.repository.ManagerDataBase import ManagerDataBase

print(ClassroomService.getByName("sala2"))

