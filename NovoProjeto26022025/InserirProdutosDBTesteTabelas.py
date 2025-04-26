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
                id_produto, nome, descricao, preco, quantidade = registo
                print(f"ID - {id_produto}")
                print(f"Nome - {nome}")
            return registos
        else:
            print("Nenhum registo encontrado.")
            return None
 
    except Error as err:
        print(f"Erro ao listar os produtos: {err}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
 
 
# Função para editar um registo
def editar_produto():
    try:
        registos = listar_produtos()
        if not registos:
            return
 
        id_editar = int(input("\nDigite o ID do produto que deseja editar: "))
 
        ids_existentes = [registo[0] for registo in registos]
        if id_editar not in ids_existentes:
            print("ID inválido. Operação cancelada.")
            return
 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtestestabelas"
        )
        mycursor = mydb.cursor()
 
        print("\nDeixe o campo em branco se não quiser alterar.")
        novo_nome = input("Novo nome: ")
        nova_descricao = input("Nova descrição: ")
        novo_preco = input("Novo preço: ")
        nova_quantidade = input("Nova quantidade: ")
 
        campos = []
        valores = []
 
        if novo_nome:
            campos.append("Produto_nome = %s")
            valores.append(novo_nome)
        if nova_descricao:
            campos.append("Produto_descrit = %s")
            valores.append(nova_descricao)
        if novo_preco:
            campos.append("Produto_preco = %s")
            valores.append(float(novo_preco))
        if nova_quantidade:
            campos.append("Produto_quantidade = %s")
            valores.append(int(nova_quantidade))
 
        if not campos:
            print("Nenhuma alteração feita. Operação cancelada.")
            return
 
        sql = f"UPDATE Produtos SET {', '.join(campos)} WHERE Produto_id = %s"
        valores.append(id_editar)
        mycursor.execute(sql, tuple(valores))
        mydb.commit()
 
        print("Produto atualizado com sucesso!")
 
    except Error as err:
        print(f"Erro ao editar o produto: {err}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
 
editar_produto()
