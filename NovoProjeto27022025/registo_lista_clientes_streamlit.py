import streamlit as st
import mysql.connector
import re
import pandas as pd

def validar_nome(nome):
    """
    Valida se o nome contém apenas letras e espaços.
    Permite letras acentuadas e apóstrofos para nomes mais completos.
    """
    return bool(re.match(r"^[a-zA-ZÀ-ú\s']+$", nome))

def validar_telefone(telefone):
    """
    Valida se o telefone contém exatamente 9 dígitos (apenas números).
    Não permite espaços, hífens, parênteses ou outros caracteres não numéricos.
    """
    return telefone.isdigit() and len(telefone) == 9

def validar_email(email):
    """
    Valida o formato do email usando uma expressão regular mais robusta.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(email_regex, email)

def validar_localidade(localidade):
    """
    Valida se a localidade contém apenas letras e espaços, similar ao nome.
    Permite letras acentuadas e hífens.
    """
    return bool(re.match(r"^[a-zA-ZÀ-ú\s\-]+$", localidade))

def conectar_bd():
    """
    Função para conectar ao banco de dados MySQL.
    Cria o banco de dados 'clientesdb' e a tabela 'clientes' se não existirem.
    Retorna um objeto de conexão ou None em caso de erro.
    """
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
        cursor = mydb.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                localidade VARCHAR(255) NOT NULL
            )
        """)
        cursor.close()
        return mydb
    except mysql.connector.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def guardar_dados(nome, telefone, email, localidade):
    """
    Guarda os dados do cliente no banco de dados após validar os campos.
    Mostra mensagens de erro e sucesso na interface Streamlit.
    """
    if not nome or not telefone or not email or not localidade:
        st.error("Por favor, preencha todos os campos.")
        return

    if not validar_nome(nome):
        st.error("Nome inválido. Use apenas letras, espaços, apóstrofos e acentos.")
        return

    if not validar_telefone(telefone):
        st.error("Telefone inválido. Insira um número de telefone com exatamente 9 dígitos (apenas números, sem espaços ou outros símbolos).") # Mensagem de erro ATUALIZADA
        return

    if not validar_email(email):
        st.error("Email inválido. Insira um email no formato correto (ex: nome@gmail.com).")
        return

    if not validar_localidade(localidade):
        st.error("Localidade inválida. Use apenas letras, espaços, hífens e acentos.")
        return

    mydb = conectar_bd()
    if not mydb:
        return

    try:
        cursor = mydb.cursor()

        # Verifica se o email já existe
        cursor.execute("SELECT email FROM clientes WHERE email = %s", (email,))
        resultado = cursor.fetchone()

        if resultado:
            st.error("Este email já está registado no sistema.")
            return

        sql = "INSERT INTO clientes (nome, telefone, email, localidade) VALUES (%s, %s, %s, %s)"
        val = (nome, telefone, email, localidade)
        cursor.execute(sql, val)
        mydb.commit()
        st.success(f"O Cliente '{nome}' foi registado com sucesso!")

    except mysql.connector.Error as e:
        st.error(f"Ocorreu um erro ao guardar os dados: {e}")
    finally:
        if mydb and mydb.is_connected():
            cursor.close()
            mydb.close()

def mostrar_clientes():
    """
    Mostra a lista de clientes registados numa tabela Streamlit.
    Se a tabela não existir ou estiver vazia, mostra uma mensagem informativa.
    """
    mydb = conectar_bd()
    if not mydb:
        return

    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES LIKE 'clientes'")
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            if resultados:
                df = pd.DataFrame(resultados, columns=["ID", "Nome", "Telefone", "Email", "Localidade"])
                st.subheader("Lista de Clientes Registados")
                st.dataframe(df)
            else:
                st.info("Não há clientes registados ainda. Registe o primeiro cliente!")
        else:
            st.info("A tabela de clientes ainda não foi criada. Registe o primeiro cliente para a criar e ver a lista.")

    except mysql.connector.Error as e:
        st.error(f"Erro ao tentar encontrar os clientes: {e}")
    finally:
        if mydb and mydb.is_connected():
            cursor.close()
            mydb.close()

def main():
    """
    Função principal que configura a interface Streamlit e gere a interação com o utilizador.
    """
    st.title("Registo de Clientes") # Título mais direto
    st.write("Preencha os detalhes do cliente abaixo para registar.")

    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome completo:")
        telefone = st.text_input("Telefone:")
    with col2:
        email = st.text_input("Email:")
        localidade = st.text_input("Localidade:")

    st.markdown("---") # Separador visual

    col_botao_guardar, col_botao_mostrar = st.columns(2)

    with col_botao_guardar:
        if st.button("Registar Cliente"):
            guardar_dados(nome, telefone, email, localidade)

    with col_botao_mostrar:
        if st.button("Mostrar Lista de Clientes"):
            mostrar_clientes()

    st.sidebar.header("Sobre este App")
    st.sidebar.info(
        "Este é um aplicativo simples para registar e visualizar clientes.\n"
        "Utiliza Streamlit para a interface e MySQL para a base de dados.\n"
        "Preencha os campos e clique em 'Registar Cliente' para adicionar um novo cliente.\n"
        "Clique em 'Mostrar Lista de Clientes' para ver todos os clientes registados."
    )

if __name__ == "__main__":
    main()
