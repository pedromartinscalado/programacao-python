import mysql.connector
from mysql.connector import Error

# Função para criar o banco de dados e a tabela Produtos
def criar_banco_de_dados_e_tabela():
    try:
        # Conectar ao MySQL
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Coloque sua senha do MySQL se necessário
        )

        # Verificar se a conexão foi bem-sucedida
        if liga.is_connected():
            print(f"Conexão com o MySQL realizada com sucesso!\n")

        mycursor = liga.cursor()

        # Criar o banco de dados
        mycursor.execute("CREATE DATABASE IF NOT EXISTS bd_bonita")
        print("Banco de dados 'bd_bonita' criado ou já existe!")

        # Selecionar o banco de dados criado
        mycursor.execute("USE bd_bonita")

        # Criar a tabela Produtos
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
                Produto_nome VARCHAR(100) NOT NULL,
                Produto_descricao TEXT,
                Produto_price DECIMAL(10, 2),
                Produto_Quantidade INT
            )
        """)
        print("Tabela 'produtos' criada ou já existe!")

        liga.commit()  # Confirmar as alterações

    except Error as err:
        print(f"Erro ao criar o banco de dados e a tabela: {err}")
    finally:
        if liga.is_connected():
            mycursor.close()
            liga.close()

# Chama a função para criar o banco de dados e a tabela
if __name__ == "__main__":
    criar_banco_de_dados_e_tabela()
