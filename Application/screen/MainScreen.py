from tkinter import *
from tkinter import ttk
from Application.screen.InsertClassroomScreen import InsertClassroomScreen


class MainScreen:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("644x482")
        self.window.resizable(False, False)
        self.window.title("Class manager")
        self.window.configure(bg="white")

        #styles
        self.styleController = ttk.Style()
        self.applyStyles()

        #buttons frame
        self.buttonsFrame = Frame(self.window)
        self.buttonsFrame.pack()

        buttonToInsertClassroom = ttk.Button(self.buttonsFrame, text="Insert Classroom", style='button.TButton', command=self.openInsertClassroomScreen)
        buttonToInsertClassroom.grid(column=0, row=0, padx=5, pady=5)



    def main(self):
        self.window.mainloop()

    def applyStyles(self):
        self.styleController.theme_use("alt")
        self.styleController.configure(
            "button.TButton",
            background="#2C2C2C",
            foreground="white",
            font=('Arial', 10, 'bold'),
            width=15,
            padding= 12,
            borderwidth=1
        )
        self.styleController.map("button.TButton", background=[('active', '#1C1C1C')])

    def openInsertClassroomScreen(self):

        InsertClassroomScreen().main()
        self.window.children.clear()


    

