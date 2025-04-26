import mysql.connector

# Função para criar o banco de dados se não existir
def criar_base_dados():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS tstore")
        print("Base de dados 'tstore' criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar a base de dados: {err}")
    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()

# Função para criar a tabela de produtos
def criar_tabela():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tstore"
        )

        if mydb.is_connected():
            print("Conexão com a base de dados realizada com sucesso!")

            mycursor = mydb.cursor()

            # Criar tabela Produtos se não existir
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Produtos (
                    Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
                    Produto_nome VARCHAR(255),
                    Produto_foto LONGBLOB,
                    Produto_price FLOAT,
                    Produto_Quantidade INT
                )
            """)

            print("Tabela 'Produtos' criada com sucesso ou já existe.")

    except mysql.connector.Error as err:
        print(f"Erro ao criar a tabela: {err}")

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()

# Executar as funções
criar_base_dados()  # Primeiro cria a base de dados
criar_tabela()      # Depois cria a tabela


##Base de dados 'tstore' criada com sucesso!
##Conexão com a base de dados realizada com sucesso!
##Tabela 'Produtos' criada com sucesso ou já existe.
