from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribos")
    #obter os resultados
    resultados = cursor.fetchall()
    # imprimir os resultados
    for resultado in resultados:
        print(resultado)
    # fechar a conexão e o cursor
    cursor.close()
    conn.close()
    