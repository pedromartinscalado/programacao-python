import mysql.connector
from mysql.connector import Error

# Função para adicionar um produto na tabela Produtos
def adicionar_produto(nome, descricao, preco, quantidade):
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

        # Construir a query INSERT para adicionar o produto
        sql = """
            INSERT INTO produtos (Produto_nome, Produto_descricao, Produto_price, Produto_Quantidade)
            VALUES (%s, %s, %s, %s)
        """
        val = (nome, descricao, preco, quantidade)

        # Executar a query
        mycursor.execute(sql, val)

        # Confirmar a inserção
        liga.commit()

        print(f"Produto '{nome}' adicionado com sucesso!")

    except Error as err:
        print(f"Erro ao adicionar o produto: {err}")
    finally:
        if liga.is_connected():
            mycursor.close()
            liga.close()

# Função principal para adicionar vários produtos
def main():
    while True:
        # Solicitar dados para o novo produto
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto (em Euros): "))
        quantidade = int(input("Digite a quantidade do produto: "))

        # Adicionar o produto
        adicionar_produto(nome, descricao, preco, quantidade)

        # Perguntar se o usuário quer adicionar outro produto
        continuar = input("\nDeseja adicionar outro produto? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
