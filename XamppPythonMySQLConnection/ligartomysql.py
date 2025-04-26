import mysql.connector


mydb = mysql.connector.connect(host='localhost',
        database = 'bd_bonita',
        user='root',
        password='')


if mydb.is_connected():
    db_info = mydb.get_server_info()
    print("Conexão realizada com sucesso ao servidor versão", db_info)
    cursor = mydb.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Ligado à base de dados: ", linha)


if mydb.is_connected():
    cursor.close()
    mydb.close()
    print("A ligação ao MySQL foi encerrada com sucesso")
