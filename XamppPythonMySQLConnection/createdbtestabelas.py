import mysql.connector
from mysql.connector import Error

def criar_base_dados():
    con = None
    cursor = None
    try:
        # Conectar ao MySQL sem especificar a base de dados
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if con.is_connected():
            cursor = con.cursor()
            # Cria a base de dados se não existir
            cursor.execute("CREATE DATABASE IF NOT EXISTS dbtestestabelas")
            print("Banco de dados 'dbtestestabelas' criado (ou já existente).")
    except Error as err:
        print(f"Erro ao criar o banco de dados: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None and con.is_connected():
            con.close()
            print("Conexão com o MySQL fechada.")

def criar_tabela():
    mydb = None
    mycursor = None
    try:
        # Conectar à base de dados
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtestestabelas"
        )
        mycursor = mydb.cursor()

        # Criar a tabela Produtos se não existir
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Produto_nome VARCHAR(100),
                Produto_descrit TEXT,
                Produto_preco DECIMAL(10, 2),
                Produto_quantidade INT
            )
        """)
        print("Tabela 'Produtos' criada (ou já existente).")
        
    except mysql.connector.Error as err:
        print(f"Erro ao criar a tabela: {err}")
    
    finally:
        if mycursor is not None:
            mycursor.close()
        if mydb is not None and mydb.is_connected():
            mydb.close()
            print("Conexão com o banco de dados fechada.")

def inserir_produto():
    mydb = None
    mycursor = None
    try:
        # Conectar à base de dados que agora existe
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtestestabelas"
        )
        mycursor = mydb.cursor()

        # Loop para inserir múltiplos produtos
        while True:
            nome = input("Nome do produto (ou digite 'sair' para terminar): ")
            if nome.lower() == 'sair':
                break

            # Loop para validar as entradas de descrição, preço e quantidade
            while True:
                try:
                    descricao = input("Descrição do produto: ")
                    preco = float(input("Preço do produto: "))
                    quantidade = int(input("Quantidade em estoque: "))
                    break  # Sai do loop se a entrada for válida
                except ValueError:
                    print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")

            sql = ("INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade) "
                   "VALUES (%s, %s, %s, %s)")
            val = (nome, descricao, preco, quantidade)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "produto inserido.")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou inserir dados: {err}")

    finally:
        if mycursor is not None:
            mycursor.close()
        if mydb is not None and mydb.is_connected():
            mydb.close()
            print("Conexão com o banco de dados fechada.")

# Primeiro, cria a base de dados (se não existir)
criar_base_dados()

# Cria a tabela Produtos (se não existir)
criar_tabela()

# Agora, insere os produtos na tabela 'Produtos'
inserir_produto()


