import mysql.connector
from mysql.connector import Error

# Função para consultar e exibir os produtos na tabela Produtos
def consultar_produtos():
    try:
        # Conectar ao banco de dados MySQL
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Coloque sua senha do MySQL se necessário
            database="bd_bonita"  # O banco de dados que já foi criado
        )

        # Verificar se a conexão foi bem-sucedida
        if liga.is_connected():
            print(f"Conexão com o banco de dados realizada com sucesso!\n")

        mycursor = liga.cursor()

        # Consultar os dados da tabela Produtos
        sql = "SELECT Produto_Id, Produto_nome, Produto_descricao, Produto_price, Produto_Quantidade FROM produtos"
        mycursor.execute(sql)

        # Obter todos os registros obtidos na consulta
        registros = mycursor.fetchall()

        # Verificar se há registros e exibi-los
        if registros:
            print("Produtos encontrados na tabela:")
            for registro in registros:
                produto_id, nome, descricao, preco, quantidade = registro
                print(f"\nID: {produto_id}")
                print(f"Nome: {nome}")
                print(f"Descrição: {descricao}")
                print(f"Preço: {preco} Euros")
                print(f"Quantidade: {quantidade} Unidades")
                print("-" * 30)  # Linha separadora entre os registros
        else:
            print("Nenhum produto encontrado na tabela.")

    except Error as err:
        print(f"Erro ao consultar os produtos: {err}")
    finally:
        if liga.is_connected():
            mycursor.close()
            liga.close()

# Chama a função para consultar os produtos
if __name__ == "__main__":
    consultar_produtos()
