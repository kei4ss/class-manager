from src.util.weekDayEnum import WeekDay
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from src.database.base import Base

class Classroom(Base):
    __tablename__ = "classroom"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())