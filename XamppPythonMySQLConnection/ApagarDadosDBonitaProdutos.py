import mysql.connector
from mysql.connector import Error

# Função para consultar e exibir os registros da tabela Produtos
def consultaprodutos():
    liga = None  # Inicializa a variável liga
    try:
        # Conectar à base de dados
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_bonita"  # Verifique se o nome do banco de dados está correto
        )

        # Verificar se a conexão foi bem-sucedida
        if liga.is_connected():
            print(f"Conexão com a base de dados realizada com sucesso!\n")

        mycursor = liga.cursor()

        # Consultar os dados da tabela Produtos
        sql = "SELECT * FROM produtos"  # Nome da tabela conforme visto no phpMyAdmin
        mycursor.execute(sql)

        # Obter todos os registros obtidos na consulta
        registros = mycursor.fetchall()

        # Verificar se há registros e exibi-los
        if registros:
            print("Registros encontrados na tabela produtos: \n")
            for registro in registros:
                id_produto, nome, descricao, preco, quantidade = registro
                print(f"ID - {id_produto}")
                print(f" Nome: {nome}")
                print(f"Descrição: {descricao}")
                print(f"Preço: {preco} Euros")
                print(f"Quantidade: {quantidade} Unidades")
                print("*" * 30)  # Linha separadora entre os registros
        else:
            print("\nNenhum registro encontrado na tabela.")
        return registros

    except Error as err:
        print(f"Erro ao consultar a tabela: {err}")
        return []
    finally:
        if liga and liga.is_connected():
            mycursor.close()
            liga.close()

# Função para apagar registros da tabela Produtos
def apagar_produto(id_produto):
    liga = None  # Inicializa a variável liga
    try:
        # Conectar à base de dados
        liga = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_bonita"  # Nome do banco de dados correto
        )

        # Verificar se a conexão foi bem-sucedida
        if liga.is_connected():
            print(f"Conexão com a base de dados realizada com sucesso!\n")

        mycursor = liga.cursor()

        # Construir a query DELETE
        sql = "DELETE FROM produtos WHERE Produto_Id = %s"  # Nome da coluna de ID corrigido
        val = (id_produto,)

        # Executar a query
        mycursor.execute(sql, val)

        liga.commit()  # Confirmar as alterações

        print(f"Registro com ID {id_produto} apagado com sucesso!")

    except Error as err:
        print(f"Erro ao apagar o registro: {err}")
    finally:
        if liga and liga.is_connected():
            mycursor.close()
            liga.close()

# Função principal para interação do usuário
def main():
    while True:
        registros = consultaprodutos()
        if not registros:
            print("Não há registros para apagar.")
            break

        print("\nRegistros disponíveis:")
        for i, registro in enumerate(registros):
            id_produto, nome, descricao, preco, quantidade = registro
            print(f"{i+1}. ID: {id_produto}, Nome: {nome}")

        try:
            opcao = int(input("\nDigite o número do registro que deseja apagar (ou 0 para sair): "))
            if opcao == 0:
                break

            if opcao < 1 or opcao > len(registros):
                print("Opção inválida. Tente novamente.")
                continue

            id_produto_a_apagar = registros[opcao-1][0]  # Obter o ID do produto selecionado

            confirmacao = input(f"Tem certeza que deseja apagar o registro {id_produto_a_apagar}? (s/n): ")
            if confirmacao.lower() == 's':
                apagar_produto(id_produto_a_apagar)
            else:
                print("Operação cancelada.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
