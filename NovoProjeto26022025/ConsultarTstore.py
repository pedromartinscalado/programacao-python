import mysql.connector
from mysql.connector import Error
 
try:
    con = mysql.connector.connect(
        host='localhost',
        database = 'tstore',
        user ='root',
        password='')
 
    cursor = con.cursor()
    consulta_sql = "select * from clientes"
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print ("\nNúmero de registos encontrados: ", cursor.rowcount)
    print ("\nApresentar os clientes inseridos na base de dados tstore")
    for linha in linhas:
        print("Cliente ID: ", linha [0])
        print("Nome: ", linha [1])
        print("Apelido: ", linha [2])
        print("Email: ", linha [3])
        print("Telefone: ", linha [4])
        print("Morada: ", linha [5])
        print("Código Postal: ", linha [6], "\n", "\n")
 
except Error as e:
    print(f"Erro ao tentar aceder à tabela clientes  {e}")
 
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print ("A ligação ao MySQL foi encerrada com sucesso")
