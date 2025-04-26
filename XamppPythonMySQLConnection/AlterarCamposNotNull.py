import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tstore"
)
mycursor = mydb.cursor()
mycursor.execute("""
    ALTER TABLE Produtos 
    MODIFY Produto_price FLOAT NOT NULL, 
    MODIFY Produto_Quantidade INT NOT NULL
""")
mydb.commit()
mycursor.close()
mydb.close()
