import mysql.connector
 
# Conexão inicial para apagar a base de dados
conexao_inicial = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
 
cursor_inicial = conexao_inicial.cursor()
cursor_inicial.execute("DROP DATABASE IF EXISTS loja_bonita")
cursor_inicial.close()
conexao_inicial.close()
 
print("A base de dados 'loja_bonita' foi apagada com sucesso.")
