import mysql.connector
from mysql.connector import Error

# Função para listar registos separados
def listar_produtos():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtestestabelas"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Produtos")
        registos = mycursor.fetchall()

        if registos:
            print("\nRegistos encontrados na tabela Produtos:\n")
            for registo in registos:
                id, nome, descricao, preco, quantidade = registo
                print(f"ID - {id}")
                print(f"Nome - {nome}")
            return registos
        else:
            print("Nenhum registo encontrado.")
            return None

    except Error as err:
        print(f"Erro ao listar os produtos: {err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()

# Função para garantir que o preço inserido seja válido
def obter_preco():
    while True:
        try:
            preco = input("Novo preço (ou pressione Enter para não alterar): ")
            if preco == "":
                return None
            preco = float(preco)
            if preco <= 0:
                print("O preço deve ser um valor positivo maior que zero. Tente novamente.")
                continue
            return preco
        except ValueError:
            print("Preço inválido. Insira um número válido para o preço.")

# Função para garantir que a quantidade inserida seja válida
def obter_quantidade():
    while True:
        try:
            quantidade = input("Nova quantidade (deve ser um número inteiro maior que zero, ou pressione Enter para não alterar): ")
            if quantidade == "":
                return None
            quantidade = int(quantidade)  # Garantir que é um inteiro
            if quantidade <= 0:
                print("A quantidade deve ser um número inteiro maior que zero. Tente novamente.")
                continue
            return quantidade
        except ValueError:
            print("Quantidade inválida. Insira um número inteiro válido para a quantidade.")

# Função para garantir que o nome e a descrição não sejam vazios ou apenas espaços
def obter_nome_ou_descricao(campo, tipo):
    while True:
        valor = input(f"{campo} (ou pressione Enter para não alterar): ").strip()  # Remover espaços no início e no final
        if valor:  # Verifica se o valor não está vazio
            return valor
        elif tipo == "nome":
            print("O nome não pode ser vazio ou conter apenas espaços. Tente novamente.")
        else:
            print("A descrição não pode ser vazia ou conter apenas espaços. Tente novamente.")

# Função para editar um registo
def editar_produto():
    mydb = None  # Inicializando mydb antes do try
    try:
        while True:  # Loop para permitir repetição
            registos = listar_produtos()
            if not registos:
                return

            while True:
                try:
                    id_editar = int(input("\nDigite o ID do produto que deseja editar: "))
                    if id_editar <= 0:
                        print("ID inválido. O ID deve ser maior que 0 e existir na lista de produtos. Operação cancelada.")
                        continue

                    # Verificar se o ID existe
                    ids_existentes = [registo[0] for registo in registos]
                    if id_editar not in ids_existentes:
                        print(f"ID {id_editar} não encontrado. Operação cancelada.")
                        continue  # Permitir que o usuário tente novamente

                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="dbtestestabelas"
                    )
                    mycursor = mydb.cursor()

                    print("\nDeixe o campo em branco se não quiser alterar.")
                    novo_nome = obter_nome_ou_descricao("Novo nome", "nome")  # Garantir nome válido
                    nova_descricao = obter_nome_ou_descricao("Nova descrição", "descricao")  # Garantir descrição válida
                    novo_preco = obter_preco()  # Validar preço
                    nova_quantidade = obter_quantidade()  # Validar quantidade

                    campos = []
                    valores = []

                    if novo_nome:
                        campos.append("Produto_nome = %s")
                        valores.append(novo_nome)
                    if nova_descricao:
                        campos.append("Produto_descrit = %s")
                        valores.append(nova_descricao)
                    if novo_preco is not None:
                        campos.append("Produto_preco = %s")
                        valores.append(novo_preco)
                    if nova_quantidade is not None:
                        campos.append("Produto_quantidade = %s")
                        valores.append(nova_quantidade)

                    if not campos:
                        print("Nenhuma alteração feita. Operação cancelada.")
                        continue  # Permitir que o usuário tente editar outro produto

                    # Substituir 'Produto_id' por 'id' que é o nome correto da coluna de ID
                    sql = f"UPDATE Produtos SET {', '.join(campos)} WHERE id = %s"
                    valores.append(id_editar)
                    mycursor.execute(sql, tuple(valores))
                    mydb.commit()

                    print("Produto atualizado com sucesso!")

                    # Perguntar se deseja editar outro produto
                    while True:
                        repetir = input("\nDeseja editar outro produto? (s/n): ").lower()
                        if repetir == "s":
                            break  # Continua o loop para editar outro produto
                        elif repetir == "n":
                            return  # Sai do loop e termina o programa
                        else:
                            print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

                    break  # Sai do loop após editar o produto

                except ValueError:
                    print("ID inválido. Por favor, insira um número válido.")
                
    except Error as err:
        print(f"Erro ao editar o produto: {err}")
    finally:
        if mydb and mydb.is_connected():
            mycursor.close()
            mydb.close()

editar_produto()


