import mysql.connector

def inserir_produto():
    try:
        # Conectar à base de dados
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

            while True:
                try:
                    descricao = input("Descrição do produto: ")

                    # Valida se o preço é positivo.
                    while True:
                        preco = float(input("Preço do produto (deve ser maior que zero): "))
                        if preco > 0:
                            break  # Sai do loop se o preço for válido
                        else:
                            print("O preço deve ser maior que zero. Tente novamente.")

                    # Valida se a quantidade é inteira e positiva.
                    while True:
                        quantidade = int(input("Quantidade em stock (deve ser maior que zero): "))
                        if quantidade > 0:
                            break  # Sai do loop se a quantidade for válida.
                        else:
                            print("A quantidade deve ser maior que zero. Tente novamente.")

                    break  # Sai do loop se todas as entradas forem válidas
                except ValueError:
                    print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")

            # Verificar se o produto já existe na base de dados
            sql_check = "SELECT COUNT(*) FROM Produtos WHERE Produto_nome = %s"
            mycursor.execute(sql_check, (nome,))
            produto_existente = mycursor.fetchone()[0]

            if produto_existente > 0:
                print(f"Produto '{nome}' já existe no banco de dados. Tente outro nome.")
            else:
                # Inserir produtos na base de dados
                sql = """INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade)
                        VALUES (%s, %s, %s, %s)"""
                val = (nome, descricao, preco, quantidade)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Produto '{nome}' inserido com sucesso! Preço: {preco} e Quantidade: {quantidade} ")

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou a inserir dados: {erro}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Conexão com a base de dados fechada.")

# Executa a função de inserção
inserir_produto()



