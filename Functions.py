from random import *
from pymongo import *

# this function will be implemented later
def connectionDB():
    z=0

def choiceUser():
    choice = input('Sua escolha: ')
    return choice

def showData():

    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client['ERP']  # acessa o database
    books = db['AleatoryNumbers']  # acessa a coleção dentro do banco de dados

    # retorna os valores dentro da coleção AleatoryNumbers
    for b in books.find():
        print(b)

def createNumbersDatabase():

    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client.ERP  # conecta com a bases de dados ERP
    col = db.AleatoryNumbers  # recupera a tabela que queremos usar

    x = 0
    seed()

    # gera numeros aleatorios e popula a coleção AleatoryNumbers
    while (x < 200):
        k = randrange(0, 200)
        col.insert_one({"id": x , "intnum": k })

        x = x + 1

def deleteData():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client.ERP  # conecta com a bases de dados ERP
    col = db.AleatoryNumbers  # recupera a tabela que queremos usar

    x = 0
    while (x < 200):
        col.delete_one({"id": x})
        x = x + 1
