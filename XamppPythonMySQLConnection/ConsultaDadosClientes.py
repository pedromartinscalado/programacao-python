import mysql.connector
from mysql.connector import Error  # Importar a classe Error

try:
    con = mysql.connector.connect(
        host='localhost',
        database='tstore',
        user='root',
        password=''
    )

    if con.is_connected():
        print("Conexão com a base de dados realizada com sucesso!")

        # Criar cursor e executar consulta
        cursor = con.cursor()
        consulta_sql = "SELECT * FROM Clientes"
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("\nNúmero de registos encontrados:", cursor.rowcount)
        print("\nApresentar os clientes inseridos na base de dados 'tstore':\n")

        # Loop para apresentar os resultados
        for linha in linhas:
            print("Cliente ID: ", linha[0])
            print("Nome: ", linha[1])
            print("Apelido: ", linha[2])
            print("Email: ", linha[3])
            print("Telefone: ", linha[4])
            print("Morada: ", linha[5])
            print("Código Postal: ", linha[6])
            print("Localidade: ", linha[7])
            print("País: ", linha[8], "\n")

except Error as e:
    print("Erro ao tentar aceder à tabela Clientes:", e)

finally:
    # Fechar cursor e conexão se existirem
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'con' in locals() and con.is_connected():
        con.close()
        print("A ligação ao MySQL foi encerrada com sucesso.")
