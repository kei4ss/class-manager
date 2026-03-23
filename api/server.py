from fastapi import FastAPI
from src.database.connection import engine, get_session
from src.database.base import Base
from src.service.classroom_service import ClassroomService

app = FastAPI()
Base.metadata.create_all(engine)
session = get_session()
classroomService = ClassroomService(session)

@app.get("/status/{parametro}")
async def root(parametro):
    return {"message": f"opa {parametro}"}

@app.post("/classroom")
def createClassroom():
    return classroomService.create("Sala de teste")

@app.get("/classroom")
def findAll():
    return classroomService.get_all()