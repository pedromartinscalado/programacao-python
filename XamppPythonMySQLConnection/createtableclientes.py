import mysql.connector

# Função para criar a tabela de clientes
def criar_tabela_clientes():
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

            # Criar tabela Clientes se não existir
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Clientes (
                    Cliente_Id INT AUTO_INCREMENT PRIMARY KEY,
                    Nome VARCHAR(100),
                    Apelido VARCHAR(100),
                    Email VARCHAR(100) UNIQUE,
                    Telefone VARCHAR(20),
                    Morada VARCHAR(255),
                    Codigo_postal VARCHAR(10),
                    Localidade VARCHAR(100),
                    País VARCHAR(50)
                )
            """)

            # Confirmar que a tabela foi criada
            print("Tabela Clientes criada com sucesso ou já existe.")

    except mysql.connector.Error as err:
        print(f"Erro ao criar a tabela: {err}")

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            
# Executar a função para criar a tabela Clientes
criar_tabela_clientes()
