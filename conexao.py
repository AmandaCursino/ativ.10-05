import mysql.connector

def conectar():
    mybd = mysql.connector.connect(
        host = 'bdfilial.c5y9ymufqwie.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'Senai123',
        database = 'tribos'
    )
    return mybd