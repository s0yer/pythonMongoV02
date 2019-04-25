from random import *
from pymongo import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# this function will be implemented later
def connectionDB():
    try:
        client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
        db = client.ERP  # conecta com a bases de dados ERP
        col = db.Numbers  # recupera a tabela que queremos usar
        return col

    except:
        return "Error of database connection..."

def makeBooks():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client['ERP']  # acessa o database
    books = db['Numbers']  # acessa a coleção dentro do banco de dados
    return books

def choiceUser():
    choice = input('Sua escolha: ')
    return choice

def showData():

    # retorna os valores dentro da coleção AleatoryNumbers
    for b in makeBooks().find():
        print(b)

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

def historicPDF(args):
    try:
        nameFile = "NumbersHistoric.pdf"
        cnv = canvas.Canvas(nameFile, pagesize= A4)
        print(A4)

        posX = mm2p(comprim/2.0 + offsetX)
        cnv.drawCentredString(posX, mm2p(posY, showData())
        cnv.save

    except:
        print("Write PDF Error... ")