import mysql.connector
from mysql.connector import Error

# Função para apagar o banco de dados
def apagar_banco_de_dados():
    try:
        # Conectar ao MySQL
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Se necessário, coloque a senha do MySQL
        )

        # Verificar se a conexão foi bem-sucedida
        if liga.is_connected():
            print(f"Conexão com o MySQL realizada com sucesso!\n")

        mycursor = liga.cursor()

        # Deletar o banco de dados
        sql = "DROP DATABASE bd_bonita"
        mycursor.execute(sql)

        liga.commit()  # Confirmar as alterações
        print("Banco de dados 'bd_bonita' apagado com sucesso!")

    except Error as err:
        print(f"Erro ao apagar o banco de dados: {err}")
    finally:
        if liga.is_connected():
            mycursor.close()
            liga.close()

# Chama a função para apagar o banco de dados
if __name__ == "__main__":
    apagar_banco_de_dados()
