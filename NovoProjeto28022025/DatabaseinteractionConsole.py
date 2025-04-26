import mysql.connector
from mysql.connector import Error
import os

def validar_entrada(column, value):
    """Valida a entrada do usuário com base na coluna."""
    if column == "NOME":
        # Permite apenas letras, espaços e caracteres portugueses
        import re
        if not re.match("^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", value) or len(value) < 2:
            return "Nome inválido. O nome deve conter apenas letras e ter pelo menos 2 caracteres."
    elif column == "IDADE":
        try:
            idade = int(value)
            if idade < 18 or idade > 85:
                return "Idade inválida. A idade deve estar entre 18 e 85 anos."
        except ValueError:
            return "Idade inválida. Por favor, insira um número inteiro."
    elif column == "SALARIO":
        try:
            salario = float(value)
            if salario < 1.00:
                return "Salário inválido. O salário mínimo deve ser 1.00."
        except ValueError:
            return "Salário inválido. Por favor, insira um número válido."
    elif column == "TELEFONE":
        if value.lower() != "null":
            if not value.isdigit() or len(value) < 9:
                return "Telefone inválido. Use apenas números com no mínimo 9 dígitos ou NULL."
    elif column == "COD_Postal":
        import re
        # Verifica se está no formato XXXX-XXX
        if not re.match(r'^\d{4}-\d{3}$', value):
            return "Código Postal inválido. Use o formato XXXX-XXX (ex: 1234-567)."
    return None

def obter_entrada(columns):
    """Obtém a entrada do usuário para cada coluna."""
    items = []
    for column in columns[1:]:
        while True:
            value = input(f"{column}: ")
            erro = validar_entrada(column, value)
            if erro:
                print(erro)
            else:
                items.append(value)
                break
    return items

def exibir_lista(info, columns):
    """Exibe a lista de pessoas."""
    if not info:
        print("Nenhum registro encontrado.")
        print("\n")
        return

    # Calculate dynamic column widths
    col_widths = []
    for i, col in enumerate(columns):
        # Get max width of column header and data
        header_width = len(str(col))
        data_width = max(len(str(row[col])) if row[col] is not None else 4 for row in info)
        col_widths.append(max(header_width, data_width) + 2)  # Add padding
    
    # Print headers
    header_row = ""
    for i, col in enumerate(columns):
        header_row += f"{str(col):<{col_widths[i]}}"
    print(header_row)
    
    # Print separator line
    print("-" * sum(col_widths))
    
    # Print data rows
    for pessoa in info:
        row = ""
        for i, col in enumerate(columns):
            value = str(pessoa[col]) if pessoa[col] is not None else "NULL"
            row += f"{value:<{col_widths[i]}}"
        print(row)
    print("\n")

def Adicionar_Pessoa(mydb):
    """Adiciona uma nova pessoa ao banco de dados."""
    try:
        pessoas, columns = selectDB(mydb, "SELECT * FROM Pessoa")
        items = obter_entrada(columns)
        confirm = input(f"\nInserir a Pessoa {items[0]}? (S/N)").strip().lower()
        if confirm == "s":
            runDB(mydb, f"insert into Pessoa ({', '.join(columns[1:])}) VALUES {tuple(items)};")
            print(f"\n{items[0]} Inserido!")
    except Error as err:
        print(f"Erro ao listar as pessoas: {err}\n\n")

def Alterar_Pessoa(mydb):
    """Altera uma pessoa existente no banco de dados."""
    while True:
        try:
            info, columns = selectDB(mydb, "SELECT * FROM Pessoa")
            IDs = [row['PessoaID'] for row in info]
            pessoas = [row['NOME'] for row in info]
            ID_name = columns[0]
            print("Pessoas Presentes:\n")
            print("\n".join([f" {i+1} - {pessoas[i]}" for i in range(len(pessoas))]))
            try:
                opcao = int(input("\nIndique o número do registro que deseja Alterar (ou 0 para cancelar): "))
                if opcao == 0:
                    print("\nCancelado.")
                    break
                if opcao < 1 or opcao > len(pessoas):
                    print("\nOpção inválida.")
                    continue
                campos = obter_entrada(columns)
                insert_SQL = ", ".join(f"{column} = '{campos[j]}'" for j, column in enumerate(columns[1:]))
                confirmacao = input(f"\n\nTem certeza que deseja substituir o registro {pessoas[opcao-1]} pelo registro {campos[0]}? (s/n): ")
                if confirmacao.lower() == 's':
                    runDB(mydb, f"UPDATE Pessoa SET {insert_SQL} WHERE {ID_name} = {IDs[opcao-1]}")
                    print(f"\n{pessoas[opcao-1]} Substituido por {campos[0]}!")
                    break
                else:
                    print("Operação cancelada.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.\n\n")
        except Error as err:
            print(f"Erro ao listar as pessoas: {err}\n\n")

def Alterar_Propriedade(mydb):
    """Altera uma propriedade específica de uma pessoa no banco de dados."""
    while True:
        try:
            info, columns = selectDB(mydb, "SELECT * FROM Pessoa")
            IDs = [row['PessoaID'] for row in info]
            pessoas = [row['NOME'] for row in info]
            ID_name = columns[0]
            print("\n\nPessoas Presentes:\n")
            print("\n".join([f" {i+1} - {pessoas[i]}" for i in range(len(pessoas))]))
            try:
                opcao_nome = int(input("\nIndique o número do registro que deseja Alterar (ou 0 para cancelar): "))
                if opcao_nome == 0:
                    print("\nCancelado.")
                    break
                if opcao_nome < 1 or opcao_nome > len(pessoas):
                    print("\nOpção inválida.")
                    continue
                print("\n".join([f" {j+1} - {columns[j+1]}" for j in range(len(columns[1:]))]))
                opcao_coluna = int(input("\nIndique o parametro que deseja Alterar (ou 0 para cancelar): "))
                if opcao_coluna == 0:
                    print("\nCancelado.")
                    break
                if (opcao_coluna < 1 or opcao_coluna > len(columns[1:])):
                    print("\nOpção inválida.")
                    continue
                while True:
                    alteraçao_unica = input(f"\n{columns[opcao_coluna]} novo/a: ")
                    erro = validar_entrada(columns[opcao_coluna], alteraçao_unica)
                    if erro:
                        print(erro)
                    else:
                        break
                insert_SQL = f"{columns[opcao_coluna]} = '{alteraçao_unica}'"
                confirmacao = input(f"\n\nTem certeza que deseja substituir o {columns[opcao_coluna]} de {pessoas[opcao_nome-1]} por {alteraçao_unica}? (s/n): ")
                if confirmacao.lower() == 's':
                    runDB(mydb, f"UPDATE Pessoa SET {insert_SQL} WHERE {ID_name} = {IDs[opcao_nome-1]}")
                    print(f"\n{pessoas[opcao_nome-1]} Substituido por {alteraçao_unica}!")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.\n\n")
        except Error as err:
            print(f"Erro ao listar as pessoas: {err}\n\n")

def Apagar_Pessoa(mydb):
    """Apaga uma pessoa do banco de dados."""
    while True:
        try:
            info, columns = selectDB(mydb, "SELECT PessoaID, NOME FROM Pessoa")
            IDs = [row['PessoaID'] for row in info]
            pessoas = [row['NOME'] for row in info]
            ID_name = columns[0]
            print("Pessoas Presentes:\n")
            print("\n".join([f" {i+1} - {pessoas[i]}" for i in range(len(pessoas))]))
            try:
                opcao = int(input("\nIndique o número do registro que deseja apagar (ou 0 para cancelar): "))
                if opcao == 0:
                    print("\nCancelado.")
                    break
                if opcao < 1 or opcao > len(pessoas):
                    print("\nOpção inválida.")
                    continue
                confirmacao = input(f"\nTem certeza que deseja apagar o registro {pessoas[opcao-1]}? (s/n): ")
                if confirmacao.lower() == 's':
                    runDB(mydb, f"DELETE FROM Pessoa WHERE {ID_name} = {IDs[opcao-1]}")
                    print(f"\n{pessoas[opcao-1]} Apagado!")
                    break
                else:
                    print("Operação cancelada.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.\n\n")
        except Error as err:
            print(f"Erro ao listar as pessoas: {err}\n\n")

def ler_tabela(mydb):
    """Lê e exibe a tabela de pessoas."""
    try:
        print("\n")
        pessoas, columns = selectDB(mydb, "SELECT * FROM Pessoa")
        exibir_lista(pessoas, columns)
        esperar_tecla()
    except Error as err:
        print(f"Erro ao listar as pessoas: {err}\n\n")

def alterar_tabela(mydb):
    """Menu para alterar a tabela de pessoas."""
    print("\n")
    try:
        açao = int(input("Que açao pretende executar? \n\n 1 - Adicionar Pessoa \n\n 2 - Alterar Pessoa \n\n 3 - Apagar Pessoa \n\n Outro - Voltar \n\n"))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n\n")
        return
    if açao == 1:
        Adicionar_Pessoa(mydb)
    elif açao == 2:
        try:
            alterar = int(input("\nPretende alterar uma pessoa na sua Totalidade (1)\nou uma propriedade de cada vez(2)?\n(ou qualquer outro para voltar ao Menu)\n\n"))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n\n")
            return
        if alterar == 1:
            Alterar_Pessoa(mydb)
        elif alterar == 2:
            Alterar_Propriedade(mydb)
        else:
            print("\nRetorno")
    elif açao == 3:
        Apagar_Pessoa(mydb)
    else:
        print("\nOpção inválida. Retornando ao menu principal.\n")
        return

def full_reboot():
    """Realiza um reboot completo do banco de dados."""
    conexao_inicial = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    try:
        cursor_inicial = conexao_inicial.cursor()
        cursor_inicial.execute("DROP DATABASE IF EXISTS vestoario_10805")
        cursor_inicial.execute("CREATE DATABASE vestoario_10805")
        cursor_inicial.execute("USE vestoario_10805")
        cursor_inicial.execute("""
        CREATE TABLE Pessoa(
            PessoaID integer NOT NULL AUTO_INCREMENT,
            NOME varchar(30) NOT NULL,
            IDADE integer NOT NULL,
            SALARIO numeric(10,2) NOT NULL,
            TELEFONE VARCHAR(25) NULL,
            COD_Postal integer,
            CONSTRAINT Pessoa_PK PRIMARY KEY (PessoaID)
        );
        """)
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (42,'António Dias',43,74000,'789654',1500);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (5,'Célia Morais',26,170000,'123456',1100);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (32,'Florinda Simões',35,147000,NULL,4000);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (37,'Isabel Espada',28,86000,NULL,1100);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (49,'José António',17,210000,NULL,1500);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (14,'Nascimento Augusto',35,220000,'456123',2300);")
        cursor_inicial.execute("INSERT INTO Pessoa (PessoaID, NOME, IDADE, SALARIO, TELEFONE, COD_Postal) VALUES (25,'Paulo Viegas',32,95000,NULL,1500);")
        conexao_inicial.commit()
        print("Reboot Completo")
    except Error as err:
        print(f"Erro ao listar as pessoas: {err}\n\n")
    finally:
        if conexao_inicial.is_connected():
            cursor_inicial.close()
            conexao_inicial.close()
            return

def openDB():
    """Abre a conexão com o banco de dados."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vestoario_10805"
        )
    except mysql.connector.errors.ProgrammingError as err:
        if (err.errno == 1049):
            print("Database 'vestoario_10805' not found. Creating database...")
            full_reboot()
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vestoario_10805"
            )
        else:
            raise
    return connection

def closeDB(mydb):
    """Fecha a conexão com o banco de dados."""
    if mydb.is_connected():
        mydb.close()

def selectDB(mydb, statement):
    """Executa uma consulta SELECT no banco de dados."""
    mycursor = mydb.cursor()
    mycursor.execute(statement)
    results = []
    columns = mycursor.column_names
    for row_fetched in mycursor.fetchall():
        results.append(dict(zip(columns, row_fetched)))
    mycursor.close()
    return results, columns

def runDB(mydb, statement):
    """Executa uma consulta de modificação no banco de dados."""
    mycursor = mydb.cursor()
    mycursor.execute(statement)
    mycursor.close()
    mydb.commit()

def ensure_table_exists(mydb):
    """Garante que a tabela Pessoa exista no banco de dados."""
    try:
        mycursor = mydb.cursor()
        mycursor.execute("USE vestoario_10805")
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Pessoa(
            PessoaID integer NOT NULL AUTO_INCREMENT,
            NOME varchar(30) NOT NULL,
            IDADE integer NOT NULL,
            SALARIO numeric(10,2) NOT NULL,
            TELEFONE VARCHAR(25) NULL,
            COD_Postal integer,
            CONSTRAINT Pessoa_PK PRIMARY KEY (PessoaID)
        );
        """)
        mycursor.close()
    except Error as err:
        print(f"Erro ao garantir a existência da tabela: {err}\n\n")

def esperar_tecla():
    """Espera o usuário pressionar uma tecla para continuar."""
    input("Pressione uma tecla para voltar... ")
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal e retorna a ação escolhida pelo usuário."""
    while True:
        try:
            açao = int(input("\nQue ação pretende executar?\n\n 1 - Ler Lista\n\n 2 - Alterar lista\n\n 0 - Sair\n\n"))
            if açao in [0, 1, 2]:
                return açao
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n\n")

def main():
    """Função principal do programa."""
    while True:
        reboot = input("Quer Fazer um Full Reboot? (S/N)  ").strip().lower()
        if reboot in ['s', 'n']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'S' para sim ou 'N' para não.\n")

    if reboot == "s":
        print("Rebooting")
        full_reboot()

    myDB = openDB()
    ensure_table_exists(myDB)

    while True:
        açao = menu_principal()
        if açao == 1:
            ler_tabela(myDB)
        elif açao == 0:
            break
        elif açao == 2:
            alterar_tabela(myDB)

    closeDB(myDB)

if __name__ == "__main__":
    main()