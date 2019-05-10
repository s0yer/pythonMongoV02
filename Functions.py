from random import *
from pymongo import *

#bibliotecas que serão utilizadas em implementações posteriores para implementação do log
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

log = "Message"

#Função referente ao log de erros quando uma função é executada
def logHistory(log):
    try:
        return print(log)

    except:
        return print("Write PDF Error... ")

# this function will be implemented later

# Faz a conexão com banco de dados para manipulação de dados
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

#Acessa banco de dados para recuperação de dados
def makeBooks():
    client = MongoClient('localhost', 27017)  # conectaem um cliente do mongoDB que esta funcionando em sua máquina
    db = client['ERP']  # acessa o database
    books = db['Numbers']  # acessa a coleção dentro do banco de dados
    log = "Acess to database OK"
    logHistory(log)

    return books

# Função que recupera dados
def showData():

    # retorna os valores dentro da coleção AleatoryNumbers
    for b in makeBooks().find():
        print(b)
    log = "Show data base"
    logHistory(log)

#Cria 200 numeros inteiros aleatórios no range de 0 - 1000
def createNumbersDatabase():

    try:
        x = 0
        seed()

        # gera numeros aleatorios e popula a coleção AleatoryNumbers
        while (x < 200):
            k = randrange(0, 1000)
            connectionDB().insert_one({"id": x , "intnum": k })

            x = x + 1

        log = "Create numbers with sucess!"
        logHistory(log)
    except:
        log = "Error to create numbers.."
        return print(log)

#Deleta os 200 numeros aleatórios criados pela função createNumbersDatabase
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

#Atualiza os valores que são igual a 100 para 0
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

