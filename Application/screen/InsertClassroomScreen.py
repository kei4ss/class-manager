from tkinter import *
from tkinter import ttk

from Application.model.entities.Classroom import Classroom
from Application.model.entities.DayWeek import DayWeek
from Application.model.service.ClassroomService import ClassroomService


class InsertClassroomScreen:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x500")
        self.window.resizable(False, False)
        self.window.title("Insert Classroom")
        self.window.configure(bg="#014040")

        # styles
        self.styleController = ttk.Style()
        self.applyStyles()

        # create a Main frame
        mainFrame = ttk.Frame(self.window, padding=10)
        mainFrame.grid()

        # Parte de preenchimento de dados das aulas
        fieldClassroomFrame = ttk.Frame(mainFrame, style="createClassroomArea.TFrame")

        labelClassroomName = ttk.Label(
            fieldClassroomFrame,
            text="Classroom name",
            style="labelAuxiliar.TLabel")
        self.fieldClassroomName = ttk.Entry(fieldClassroomFrame, width=20)

        labelClassroomDay = ttk.Label(
            fieldClassroomFrame,
            text="Classroom day",
            style="labelAuxiliar.TLabel")
        self.dayChoose = ttk.Combobox(fieldClassroomFrame,
                                      values=DayWeek.getAllDayWeeks(),
                                      state="readonly")
        self.dayChoose.current(0)

        labelClassroomPrice = ttk.Label(
            fieldClassroomFrame,
            text="Classroom price",
            style="labelAuxiliar.TLabel")
        self.priceChoose = ttk.Combobox(fieldClassroomFrame,
                                        values=["30", "45"],
                                        state="readonly")
        self.priceChoose.current(0)

        btnSend = ttk.Button(
            fieldClassroomFrame,
            text="Salvar classroom",
            command=self.saveNewClassroom,
            style="createClassFrame.button.TButton")

        fieldClassroomFrame.grid()
        labelClassroomName.grid(column=1, row=0)
        self.fieldClassroomName.grid(column=1, row=1, padx=5)
        labelClassroomDay.grid(column=2, row=0)
        self.dayChoose.grid(column=2, row=1, padx=5)
        labelClassroomPrice.grid(column=3, row=0)
        self.priceChoose.grid(column=3, row=1, padx=5)

        btnSend.grid(column=2, row=3, pady=10)

    def main(self):
        self.window.mainloop()

    def saveNewClassroom(self):
        newClassroom = Classroom()
        newClassroom.setName(self.fieldClassroomName.get())
        newClassroom.setPrice(self.dayChoose.get())
        newClassroom.setDayOfWeek(DayWeek.stringToDayWeek(self.dayChoose.get()))

        if (ClassroomService.insert(newClassroom)):
            print("Class room inserted")
        else:
            print("Class room not inserted")

    def applyStyles(self):
        self.styleController.theme_use("alt")
        self.styleController.configure(
            "createClassroomArea.TFrame",
            background="#02735E",
            padding=10)
        self.styleController.configure(
            "labelAuxiliar.TLabel",
            background="#02735E",
            font=('Arial', 9, 'bold'),
            foreground="black",
            padding=5
        )
        self.styleController.configure(
            "createClassFrame.button.TButton",
            background="#F27405",
            foreground="black",
            font=('Arial', 9, 'bold'),
            width=20
        )
        self.styleController.map("createClassFrame.button.TButton", background=[('active', '#731702')])


