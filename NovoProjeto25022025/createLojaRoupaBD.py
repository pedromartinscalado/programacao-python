import mysql.connector
 
# Conexão inicial para criar a base de dados
conexao_inicial = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
 
cursor_inicial = conexao_inicial.cursor()
cursor_inicial.execute("CREATE DATABASE IF NOT EXISTS Loja_Roupa_BD")
cursor_inicial.close()
conexao_inicial.close()
 
# Verificar se a conexão à base de dados foi criada
mydb = mysql.connector.connect(
    host='localhost',
    database='Loja_Roupa_BD',
    user='root',
    password=''
)
 
if mydb.is_connected():
    db_info = mydb.get_server_info()
    print("Conexão realizada com sucesso ao servidor versão: ", db_info)
    cursor = mydb.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("Ligado à base de dados: ", linha)
 
# Fechar a ligação
if mydb.is_connected():
    cursor.close()
    mydb.close()
    print("A ligação ao MySQL foi encerrada com sucesso")
