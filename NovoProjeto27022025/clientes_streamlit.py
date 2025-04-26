import streamlit as st
import mysql.connector
import re

def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_telefone(telefone):
    return telefone.isdigit()

def validar_email(email):
    email_regex = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.fullmatch(email_regex, email)

def conectar_bd():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS clientesdb")
        cursor.close()
        mydb.close()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clientesdb"
        )
        return mydb
    except mysql.connector.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def guardar_dados(nome, telefone, email, localidade):
    if not nome or not telefone or not email or not localidade:
        st.error("Por favor, preencha todos os campos.")
        return

    if not validar_nome(nome):
        st.error("Nome inválido. Por favor, use apenas letras e espaços.")
        return

    if not validar_telefone(telefone):
        st.error("Telefone inválido. Por favor, use apenas números.")
        return

    if not validar_email(email):
        st.error("Email inválido. Por favor, insira um email no formato correto.")
        return

    mydb = conectar_bd()
    if not mydb:
        return

    try:
        cursor = mydb.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                email VARCHAR(255) NOT NULL,
                localidade VARCHAR(255) NOT NULL
            )
        """)
        sql = "INSERT INTO clientes (nome, telefone, email, localidade) VALUES (%s, %s, %s, %s)"
        val = (nome, telefone, email, localidade)
        cursor.execute(sql, val)
        mydb.commit()
        st.success("O Cliente foi registado com sucesso!")

    except mysql.connector.Error as e:
        st.error(f"Ocorreu um erro ao guardar os dados: {e}")
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

def main():
    st.title("Registar Novo Cliente")
    st.write("Por favor, preencha os detalhes do cliente abaixo.")

    nome = st.text_input("Nome:")
    telefone = st.text_input("Telefone:")
    email = st.text_input("Email:")
    localidade = st.text_input("Localidade:")

    if st.button("Guardar"):
        guardar_dados(nome, telefone, email, localidade)

if __name__ == "__main__":
    main()
