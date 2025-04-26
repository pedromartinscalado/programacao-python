import mysql.connector

def inserir_produto():
    try:
        # Conectar ao banco de dados
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tstore'
        )
        mycursor = mydb.cursor()

        # Loop para inserir múltiplos produtos
        while True:
            nome = input("Nome do produto (ou digite 'sair' para terminar): ")
            if nome.lower() == 'sair':
                break

            # Neste exemplo, não usamos uma descrição, pois a tabela não a possui.
            # Para a foto, usaremos None, indicando que não há imagem.
            foto = None

            # Loop para validar as entradas de preço e quantidade
            while True:
                try:
                    preco = float(input("Preço do produto: "))
                    quantidade = int(input("Quantidade em stock/estoque: "))
                    break  # Sai do loop se a entrada for válida
                except ValueError:
                    print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")

            # Inserir o produto na tabela
            sql = "INSERT INTO Produtos (Produto_nome, Produto_foto, Produto_price, Produto_Quantidade) VALUES (%s, %s, %s, %s)"
            val = (nome, foto, preco, quantidade)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "produto inserido.")

    except mysql.connector.Error as err:
        print("Erro ao conectar ou inserir dados:", err)

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("Conexão com o banco de dados fechada.")

# Executa a função para inserção
inserir_produto()

