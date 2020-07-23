from random import *
from pymongo import *

# bibliotecas que serão utilizadas em implementações posteriores para implementação do log
# libraries that will be used in later deployments for log implementation
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4

log = "Message"

# Função referente ao log de erros quando uma função é executada / Function regarding error log when a function is executed
def logHistory(log):
    try:
        return print(log)

    except:
        return print("Write PDF Error... ")


# Faz a conexão com banco de dados para manipulação de dados /  Make connection to database for data manipulation
def connectionDB():
    try:
        client = MongoClient('localhost', 27017)  # conecta em um cliente do mongoDB que esta funcionando em sua máquina / connects on a mongoDB client that is running on your machine
        db = client.ERP  # conecta com a bases de dados ERP / connects to ERP databases
        col = db.Numbers  # recupera a tabela que queremos usar / retrieve the table we want to use
        log = "Connection of DataBase OK"
        logHistory(log)
        return col

    except:
        log = "Error of database connection..."
        return log

# Acessa banco de dados para recuperação de dados / Access database for data recovery
def makeBooks():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina / connect a mongoDB client running on your machine
    db = client['ERP']  # acessa o database / access the database
    books = db['Numbers']  # acessa a coleção dentro do banco de dados / accesses the collection within the database
    log = "Acess to database OK"
    logHistory(log)

    return books

# Função que retorna dados / Function that returns data
def showData():

    # retorna os valores dentro da coleção AleatoryNumbers / returns values within the AleatoryNumbers collection
    for b in makeBooks().find():
        print(b)
    log = "Show data base"
    logHistory(log)

# Cria 200 numeros inteiros aleatórios no range de 0 - 1000 / Creates 200 random integers in the 0 - 1000 range
def createNumbersDatabase():

    try:
        x = 0
        seed()

        # gera numeros aleatorios e popula a coleção AleatoryNumbers / generates random numbers and populates the AleatoryNumbers collection
        while (x < 200):
            k = randrange(0, 1000)
            connectionDB().insert_one({"id": x , "intnum": k })

            x = x + 1

        log = "Create numbers with sucess!"
        logHistory(log)
    except:
        log = "Error to create numbers.."
        return print(log)

# Deleta os 200 numeros aleatórios criados pela função createNumbersDatabase / Delete the 200 random numbers created by the createNumbersDatabase

    try:
        x = 0
        while (x < 200):
            connectionDB().delete_one({"id": x})
            x = x + 1
        log = "Detele data with sucess!"
        logHistory(log)

    except:
        log = "Error to delete data.."
        return print(log)

# Atualiza os valores que são igual a 100 para 0 / Updates values that are equal to 100 for 0

def updateData():

    try:
        for b in makeBooks().find():
            connectionDB().update({"intnum": 100},{"$set":{"intnum": 0}})
            print(b)
        log = "Update Database with sucess!"
        logHistory(log)
    except:
        log = "Error to update DataBase.."
        return print(log)

