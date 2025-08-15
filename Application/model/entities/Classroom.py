from typing import override

from Application.model.entities.DayWeek import DayWeek


class Classroom:
    def __init__(self, id:int=None, name:str=None, price:int=None, dayOfWeek:DayWeek=None):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__dayOfWeek = dayOfWeek


    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getDayOfWeek(self):
        return self.__dayOfWeek

    def setName(self, name:str):
        self.__name = name
    def setPrice(self, price:int):
        self.__price = price
    def setDayOfWeek(self, dayOfWeek:DayWeek):
        self.__dayOfWeek = dayOfWeek

    @override
    def __str__(self):
        return f"{self.__name} | R${self.__price} ({self.__dayOfWeek})"
