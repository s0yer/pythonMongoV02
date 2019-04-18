from random import *
from pymongo import *

# this function will be implemented later
def connectionDB():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client.ERP  # conecta com a bases de dados ERP
    col = db.Numbers  # recupera a tabela que queremos usar
    return col

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