from enum import Enum

class DayWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    def __str__(self):
        return self.name

    @staticmethod
    def stringToDayWeek(string):
        if string == "Monday":
            return DayWeek.Monday
        elif string == "Tuesday":
            return DayWeek.Tuesday
        elif string == "Wednesday":
            return DayWeek.Wednesday
        elif string == "Thursday":
            return DayWeek.Thursday
        elif string == "Friday":
            return DayWeek.Friday
        elif string == "Saturday":
            return DayWeek.Saturday
        elif string == "Sunday":
            return DayWeek.Sunday

    @staticmethod
    def getAllDayWeeks():
        dayList = [
            DayWeek.Monday.name,
            DayWeek.Tuesday.name,
            DayWeek.Wednesday.name,
            DayWeek.Thursday.name,
            DayWeek.Friday.name,
            DayWeek.Saturday.name,
            DayWeek.Sunday.name
        ]
        return dayList