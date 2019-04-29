from random import *
from pymongo import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

log = "Message"

# this function will be implemented later
def connectionDB(String log):
    try:
        client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
        db = client.ERP  # conecta com a bases de dados ERP
        col = db.Numbers  # recupera a tabela que queremos usar
        log = "Connection of DataBase OK"
        logHistory()
        return col

    except:
        log = "Error of database connection..."
        return log

def makeBooks(String log):
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client['ERP']  # acessa o database
    books = db['Numbers']  # acessa a coleção dentro do banco de dados
    log = "Acess to database OK"
    logHistory()

    return books

def choiceUser():
    choice = input('Sua escolha: ')
    return choice

def showData():

    # retorna os valores dentro da coleção AleatoryNumbers
    for b in makeBooks().find():
        print(b)
    log = " Show data base"
    logHistory()

def createNumbersDatabase():

    x = 0
    seed()

    # gera numeros aleatorios e popula a coleção AleatoryNumbers
    while (x < 200):
        k = randrange(0, 200)
        connectionDB().insert_one({"id": x , "intnum": k })

        x = x + 1

def deleteData():

    x = 0
    while (x < 200):
        connectionDB().delete_one({"id": x})
        x = x + 1

def updateData():

    for b in makeBooks().find():
        connectionDB().update({"intnum": 100},{"$set":{"intnum": 300}})
        print(b)

def logHistory():
    try:
        nameFile = "NumbersHistoric.pdf"
        cnv = canvas.Canvas(nameFile, pagesize= A4)
        print(A4)

        posX = mm2p(comprim/2.0 + offsetX)
        cnv.drawCentredString(posX, mm2p(posY, showData())
        cnv.save()

        return print(log)

    except:

        return print("Write PDF Error... ")