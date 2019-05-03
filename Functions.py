from random import *
from pymongo import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

log = "Message"

def logHistory(log):
    try:
        return print(log)

    except:
        return print("Write PDF Error... ")

# this function will be implemented later
def connectionDB():
    try:
        client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
        db = client.ERP  # conecta com a bases de dados ERP
        col = db.Numbers  # recupera a tabela que queremos usar
        log = "Connection of DataBase OK"
        logHistory(log)
        return col

    except:
        log = "Error of database connection..."
        return log

def makeBooks():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client['ERP']  # acessa o database
    books = db['Numbers']  # acessa a coleção dentro do banco de dados
    log = "Acess to database OK"
    logHistory(log)

    return books


def showData():

    # retorna os valores dentro da coleção AleatoryNumbers
    for b in makeBooks().find():
        print(b)
    log = "Show data base"
    logHistory(log)

def createNumbersDatabase():

    try:
        x = 0
        seed()

        # gera numeros aleatorios e popula a coleção AleatoryNumbers
        while (x < 200):
            k = randrange(0, 200)
            connectionDB().insert_one({"id": x , "intnum": k })

            x = x + 1

        log = "Create numbers with sucess!"
        logHistory(log)
    except:
        log = "Error to create numbers.."
        return print(log)

def deleteData():

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

def updateData():

    try:
        for b in makeBooks().find():
            connectionDB().update({"intnum": 100},{"$set":{"intnum": 300}})
            print(b)
        log = "Update Database with sucess!"
        logHistory(log)
    except:
        log = "Error to update DataBase.."
        return print(log)

