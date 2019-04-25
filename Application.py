from Functions import *
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="CRUD Program")
        self.msg.pack()

        self.create = Button(self.widget1)
        self.create["text"] = "Create numbers Database"
        self.create["font"] = ("Arial", "9")
        self.create["width"] = 23
        self.create["command"] = self.createNumDB
        self.create.pack()

        self.delete = Button(self.widget1)
        self.delete["text"] = "Delete Data"
        self.delete["font"] = ("Arial", "9")
        self.delete["width"] = 16
        self.delete["command"] = self.delNumDB
        self.delete.pack()

        self.show = Button(self.widget1)
        self.show["text"] = "Show Database"
        self.show["font"] = ("Arial", "9")
        self.show["width"] = 16
        self.show["command"] = self.showDB
        self.show.pack()

        self.update = Button(self.widget1)
        self.update["text"] = "Update Data"
        self.update["font"] = ("Arial", "9")
        self.update["width"] = 16
        self.update["command"] = self.updateDB
        self.update.pack()

        self.exit = Button(self.widget1)
        self.exit["text"] = "Exit GUI"
        self.exit["font"] = ("Arial", "9")
        self.exit["width"] = 16
        self.exit["command"] = self.widget1.quit
        self.exit.pack()

        self.pdf = Button(self.widget1)
        self.pdf["text"] = "Write in PDF"
        self.pdf["font"] = ("Arial", "9")
        self.pdf["width"] = 16
        self.pdf["command"] = self.writePDF
        self.pdf.pack()

    def createNumDB(self):
        createNumbersDatabase()

    def delNumDB(self):
        deleteData()

    def showDB(self):
        showData()

    def updateDB(self):
        updateData()

    def writePDF(selfs):
        historicPDF()


root = Tk()
Application(root)
root.mainloop()

waitEntry = True

while waitEntry == True:
    print('Choose the option: ')
    print('c: Create new number in the Database')
    print('s: Show de coletion in the Database')
    print('u: Update colection')
    print('d: Delete the values into the coletion')
    print('e: Exit. ')

    choice = choiceUser()

    if choice == 'c':
        createNumbersDatabase()

    elif choice == 's':
        showData()

    elif choice == 'u':
        updateData()

    elif choice == 'd':
        deleteData()

    elif choice == 'e':
        waitEntry = False

    else:
        print('Invalid input, take a value from the options! ')
        waitEntry = True
