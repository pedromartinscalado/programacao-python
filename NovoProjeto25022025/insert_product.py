import mysql.connector as mysql

VERMELHO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"

def connect():
    try:
        connection = mysql.connect(
            host="localhost",
            user="luiz",
            password="",
            database="aula_python"
        )
        return connection
    except mysql.Error as erro:
        print(f"{VERMELHO}Erro ao conectar: {RESET}{erro}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos (
            productId INT AUTO_INCREMENT PRIMARY KEY,
            productName VARCHAR(200) UNIQUE NOT NULL,
            productDescri VARCHAR(1600),            
            productPrice FLOAT NOT NULL CHECK (productPrice > 0),
            productQuantity INT NOT NULL CHECK (productQuantity > 0)
        )
        """)
        connection.commit()
        print(f"{VERDE}Tabela 'Produtos' verificada/criada com sucesso!{RESET}")
        cursor.close()
    except mysql.Error as erro:
        print(f"{VERMELHO}Erro ao criar tabela: {RESET}{erro}")

def product_exists(connection, name):
    #Verifica se o produto ja existe na tabela.
    try:
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM Produtos WHERE productName = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] > 0
    except mysql.Error as erro:
        print(f"{VERMELHO}Erro ao verificar produto: {RESET}{erro}")
        return False

def insert_product(connection, name, description, price, quantity):
    #Insere um produto no banco de dados apenas se ele ainda nao existir.
    try:
        if product_exists(connection, name):
            print(f"{VERMELHO}O produto '{name}' já existe na base de dados.{RESET}")
            return
        
        cursor = connection.cursor()
        query = '''
        INSERT INTO Produtos (productName, productDescri, productPrice, productQuantity)
        VALUES (%s, %s, %s, %s)
        '''
        values = (name, description, price, quantity)
        cursor.execute(query, values)
        connection.commit()
        print(f"{VERDE}Produto '{name}' inserido com sucesso!{RESET}")
        cursor.close()
    except mysql.Error as erro:
        print(f"{VERMELHO}Erro ao inserir produto: {RESET}{erro}")

def main():
    connection = connect()
    if connection and connection.is_connected():
        print(f"{VERDE}Ligação com a base de dados realizada com sucesso!{RESET}")
        create_table(connection)

        insert_product(connection, "Teclado Gamer", "Teclado mecânico RGB", 149.99, 10)
        insert_product(connection, "Teclado Gamer", "Teclado mecânico RGB", 149.99, 10)
        
        connection.close()
        print(f"{VERDE}Conexão encerrada com sucesso!{RESET}")
    else:
        print(f"{VERMELHO}Falha ao conectar com a base de dados.{RESET}")

main()
