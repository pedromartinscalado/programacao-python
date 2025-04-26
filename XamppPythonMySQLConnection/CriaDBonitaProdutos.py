import mysql.connector

# Função para criar o banco de dados se não existir
def minhatabela():
    try:
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        mycursor = liga.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS bd_bonita")
        print("Base de dados 'bd_bonita' criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar a base de dados: {err}")
    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'liga' in locals() and liga.is_connected():
            liga.close()

# Função para criar a tabela de produtos
def criar_tabela():
    try:
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_bonita"
        )

        if liga.is_connected():
            print("Conexão com a base de dados realizada com sucesso!")

            mycursor = liga.cursor()

            # Criar tabela Produtos se não existir
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Produtos (
                    Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
                    Produto_nome VARCHAR(255),
                    Produto_descricao VARCHAR(100),
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
        if 'liga' in locals() and liga.is_connected():
            liga.close()

# Executar as funções
minhatabela()  # Primeiro cria a base de dados
criar_tabela()      # Depois cria a tabela


##Base de dados 'tstore' criada com sucesso!
##Conexão com a base de dados realizada com sucesso!
##Tabela 'Produtos' criada com sucesso ou já existe.
