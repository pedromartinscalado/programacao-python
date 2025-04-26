import mysql.connector #classe ou biblioteca
 
# Função para criar a tabela de produtos
def criar_tabela():
    try:
        # Conectar à base de dados
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_roupa_bd"
        )
        # Verificar se a conexão foi bem-sucedida
        if mydb.is_connected():
            print("Ligação com a base de dados realizada com sucesso!")
        meucursor = mydb.cursor()
 
        # Criar tabela Produtos se não existir
        meucursor.execute("""
        CREATE TABLE IF NOT EXISTS EmStock (
            Item_Id INT AUTO_INCREMENT PRIMARY KEY,
            Item_nome VARCHAR(200),
            Item_roupa TINYINT(1),
            Item_Assessorie TINYINT(1),              
            Item_descrit VARCHAR(1600),            
            Item_price FLOAT,
            Item_quantidade INT)
        """)
        # Confirmar que a tabela foi criada
        print("Tabela Produtos criada com sucesso ou já existe.")
    except mysql.connector.Error as erro:
        print(f"Erro ao criar a tabela: {erro}")
    finally:
        if mydb.is_connected():
            meucursor.close()
            mydb.close()
 
# Utilizar a função criar_tabela
criar_tabela()

