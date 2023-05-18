from conexao import conectar

def listar(conn, cursor):
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tribo")
    resultados = cursor.fetchall()
   
    for resultado in resultados:
        print(resultado)
   
    cursor.close()
    conn.close()
    
def inserir(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'INSERT INTO tribo (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar) VALUES (%s, %s, %s, %s, %s)'
    val = (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)
    cursor.execute(sql, val)
    
    conn.commit()
    
    print('Registro inserido com sucesso.')
    
    cursor.close()
    conn.close()

def deletar(codigo):
    
    conn = conectar()
    cursor = conn.cursor()
   
    sql = 'DELETE FROM tribo WHERE codigo = %s'
    val = (codigo,)
    cursor.execute(sql, val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
        print('Nenhum registro deletado.')
    else:
        print('Registro deletado com sucessor')
    
    cursor.close()
    conn.close()

conn = conectar()

cursor = conn.cursor()

while True:
  
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Deletar uma tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    
    listar(conn, cursor)
  
  elif opcao == 2:
    
    nome_tribo = input("Digite nome da nova tribo: ")
    num_hab = int(input("Digite o num de habitantes da nova tribo: "))
    renda_mensal = input("Digite a renda mensal: ")
    escolaridade = input("Digite a escolaridade da nova tribo: ")
    trab_salar = input("Digite se possuem trabalho assalariado: ")
    
    inserir(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)

  elif opcao == 3:
    
    codigo = int(input("Digite o código da tribo que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    
    break

  else:
    print("Opção inválida. Digite novamente.")
    
    
cursor.close()
conn.close()






