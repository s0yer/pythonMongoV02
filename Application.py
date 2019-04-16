from Functions import *

waitEntry = True

while waitEntry==True:
    print('Escolha a opção: ')
    print('c: Create new number in the Database')
    print('s: Show de coletion in the Database')
    print('u: -')
    print('d: Delete the values into the coletion')
    print('h: -')
    print('o: -')
    print('e: Exit. ')

    choice = choiceUser()

    if choice == 'c':
        createNumbersDatabase()

    elif choice == 's':
        showData()

    elif choice == 'u':
        waitEntry = False

    elif choice == 'd':
        deleteData()

    elif choice == 'e':
        waitEntry = False

    else:
        print('Invalid input, take a value from the options! ')
