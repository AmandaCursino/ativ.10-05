import mysql.connector

config = {
  'user': 'admin',
  'password': 'Senai123',
  'host': 'bdfilial.c5y9ymufqwie.us-east-1.rds.amazonaws.com',
  'database': 'tribos'
}
'''
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

cursor = conn.cursor()

nome_tribo = input("Digite o nome da tribo: ")
num_hab = int(input("Digite o numero de habitantes: "))
renda_mensal = int(input("Digite a renda mensal: "))
escolaridade = input("Digite o nivel de escolaridade: ")
trab_salar = input("Responda se possui trabalho assalariado (s/n): ")


sql = "INSERT INTO tribo (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar) VALUES (%s, %s)"
val = (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()
'''