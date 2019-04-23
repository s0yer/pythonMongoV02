from Functions import *
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="CRUD Program")
        self.msg.pack()

        self.sair = Button(self.widget1)
        self.sair["text"] = "Exit"
        self.sair["font"] = ("Arial", "9")
        self.sair["width"] = 6
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

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
