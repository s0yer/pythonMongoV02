from Functions import *

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
