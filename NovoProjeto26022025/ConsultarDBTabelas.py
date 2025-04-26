import mysql.connector
from mysql.connector import Error

def selecionar_base_de_dados(databases):
    while True:
        try:
            db_choice = input("\nSelecione uma base de dados (digite o número correspondente ou o nome): ").strip()
            selected_db = None
            if db_choice.isdigit():
                db_index = int(db_choice)
                if 1 <= db_index <= len(databases):
                    selected_db = databases[db_index - 1][0]
                else:
                    print("Número inválido. Tente novamente.")
                    continue
            else:
                if db_choice in [db[0] for db in databases]:
                    selected_db = db_choice
                else:
                    print("Nome da base de dados inválido. Tente novamente.")
                    continue
            return selected_db
        except Exception as e:
            print(f"Erro ao selecionar a base de dados: {e}")

def selecionar_tabela(tables):
    while True:
        try:
            table_choice = input("\nSelecione uma tabela (digite o número correspondente ou o nome): ").strip()
            selected_table = None
            if table_choice.isdigit():
                table_index = int(table_choice)
                if 1 <= table_index <= len(tables):
                    selected_table = tables[table_index - 1][0]
                else:
                    print("Número inválido. Tente novamente.")
                    continue
            else:
                if table_choice in [table[0] for table in tables]:
                    selected_table = table_choice
                else:
                    print("Nome da tabela inválido. Tente novamente.")
                    continue
            return selected_table
        except Exception as e:
            print(f"Erro ao selecionar a tabela: {e}")

def exibir_conteudo_tabela(cursor, selected_table):
    while True:
        exibir_conteudo = input(f"\nDeseja ver o conteúdo da tabela '{selected_table}'? (s/n): ").strip().lower()
        if exibir_conteudo == 's':
            try:
                cursor.execute(f"SELECT * FROM {selected_table}")
                rows = cursor.fetchall()
                if rows:
                    print(f"\nConteúdo da tabela '{selected_table}':")
                    for row in rows:
                        print(row)
                else:
                    print(f"\nA tabela '{selected_table}' está vazia.")
            except Error as e:
                print(f"Erro ao consultar a tabela {selected_table}: {e}")
            break  # Sai do loop quando o conteúdo for exibido
        elif exibir_conteudo == 'n':
            print("Você escolheu não ver o conteúdo da tabela.")
            break  # Sai do loop se não quiser ver o conteúdo
        else:
            print("Resposta inválida. Por favor, insira 's' para sim ou 'n' para não.")

try:
    # Conecta ao servidor MySQL sem especificar uma base de dados
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    
    if con.is_connected():
        cursor = con.cursor()
        
        # Listar todas as bases de dados
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Bases de dados disponíveis:")
        for i, (db,) in enumerate(databases, 1):
            print(f"{i}. {db}")
        
        # Selecionar uma base de dados
        selected_db = selecionar_base_de_dados(databases)
        
        try:
            cursor.execute(f"USE {selected_db}")
        except Error as e:
            print(f"Erro ao acessar a base de dados {selected_db}: {e}")
            exit(1)
        
        # Listar as tabelas da base de dados selecionada
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if not tables:
            print("Nenhuma tabela encontrada nesta base de dados.")
        else:
            print(f"\nTabelas na base de dados '{selected_db}':")
            for j, (table,) in enumerate(tables, 1):
                print(f"{j}. {table}")
            
            # Selecionar uma tabela
            selected_table = selecionar_tabela(tables)
            
            # Exibir a estrutura da tabela
            exibir_estrutura = input(f"\nDeseja ver a estrutura da tabela '{selected_table}'? (s/n): ").strip().lower()
            if exibir_estrutura == 's':
                try:
                    cursor.execute(f"DESCRIBE {selected_table}")
                    columns = cursor.fetchall()
                    print(f"\nEstrutura da tabela '{selected_table}':")
                    for column in columns:
                        print(f"- {column[0]}: {column[1]}")
                except Error as e:
                    print(f"Erro ao descrever a tabela {selected_table}: {e}")
            
            # Exibir o conteúdo da tabela
            exibir_conteudo_tabela(cursor, selected_table)

except Error as e:
    print(f"Erro na conexão ou execução: {e}")
    
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("\nA ligação ao MySQL foi encerrada com sucesso")


