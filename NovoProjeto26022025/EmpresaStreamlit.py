import streamlit as st
import mysql.connector

# Criar a base de dados antes de a usar
def cria_base():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS empresa;")
    cursor.close()
    conexao.close()

# Função para conectar à base de dados
def liga_base():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa"
    )

# Criar a base de dados antes de inicializar a aplicação
cria_base()

# Criar a tabela se não existir
def base():
    conexao = liga_base()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            cargo VARCHAR(50),
            salario DECIMAL(10,2)
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

# Inicializar a tabela
base()

# Função para adicionar funcionários
def adicionar_funcionarios(nome, cargo, salario):
    conexao = liga_base()
    cursor = conexao.cursor()
    sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, cargo, salario))
    conexao.commit()
    cursor.close()
    conexao.close()

# Função para obter todos os funcionários
def obter_funcionarios():
    conexao = liga_base()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios;")
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados

# Interface com Streamlit
st.title("Registo dos Funcionários")

# Formulário de entrada
nome = st.text_input("Nome")
cargo = st.text_input("Cargo")
salario = st.number_input("Salário", min_value=0.0, format="%.2f")

if st.button("Adicionar Funcionário"):
    if nome and cargo and salario > 0:
        adicionar_funcionarios(nome, cargo, salario)
        st.success("Funcionário registado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")

# Exibir funcionários registados
st.subheader("Funcionários Registados")
dados = obter_funcionarios()

if dados:
    for funcionario in dados:
        st.write(f"**ID:** {funcionario[0]} | **Nome:** {funcionario[1]} | **Cargo:** {funcionario[2]} | **Salário:** €{funcionario[3]:,.2f}")
else:
    st.info("Nenhum funcionário registado na base de dados.")

