import streamlit as st
import mysql.connector
from mysql.connector import Error

# Função para conectar à base de dados
def liga_base():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="empresa"
        )
    except Error as e:
        st.error(f"Erro ao conectar à base de dados: {e}")
        return None

# Criar a base de dados e a tabela se não existirem
def base():
    conexao = liga_base()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS empresa;")
        cursor.execute("USE empresa;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                cargo VARCHAR(50),
                salario DECIMAL(10,2)
            );
        """)
        conexao.commit()
    except Error as e:
        st.error(f"Erro ao criar a base de dados ou tabela: {e}")
    finally:
        cursor.close()
        conexao.close()

# Função para adicionar funcionários
def adicionar_funcionario(nome, cargo, salario):
    conexao = liga_base()
    if conexao is None:
        return
    cursor = conexao.cursor()
    # Verificar se o funcionário já existe
    cursor.execute("SELECT * FROM funcionarios WHERE nome = %s AND cargo = %s", (nome, cargo))
    funcionario_existente = cursor.fetchone()
    if funcionario_existente:
        st.warning(f"O funcionário {nome} já está registado com o cargo {cargo}.")
        return
    sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (nome, cargo, salario))
        conexao.commit()
    except Error as e:
        st.error(f"Erro ao adicionar funcionário: {e}")
    finally:
        cursor.close()
        conexao.close()

# Função para obter todos os funcionários
def obter_funcionarios():
    conexao = liga_base()
    if conexao is None:
        return []
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM funcionarios;")
        dados = cursor.fetchall()
    except Error as e:
        st.error(f"Erro ao obter funcionários: {e}")
        dados = []
    finally:
        cursor.close()
        conexao.close()
    return dados

# Função para atualizar um funcionário
def atualizar_funcionario(id, nome, cargo, salario):
    conexao = liga_base()
    if conexao is None:
        return
    cursor = conexao.cursor()
    sql = "UPDATE funcionarios SET nome = %s, cargo = %s, salario = %s WHERE id = %s"
    try:
        cursor.execute(sql, (nome, cargo, salario, id))
        conexao.commit()
    except Error as e:
        st.error(f"Erro ao atualizar funcionário: {e}")
    finally:
        cursor.close()
        conexao.close()

# Função para remover um funcionário
def remover_funcionario(id):
    conexao = liga_base()
    if conexao is None:
        return
    cursor = conexao.cursor()
    sql = "DELETE FROM funcionarios WHERE id = %s"
    try:
        cursor.execute(sql, (id,))
        conexao.commit()
    except Error as e:
        st.error(f"Erro ao remover funcionário: {e}")
    finally:
        cursor.close()
        conexao.close()

# Função para remover múltiplos funcionários selecionados
def remover_funcionarios_selecionados(ids):
    conexao = liga_base()
    if conexao is None:
        return
    cursor = conexao.cursor()
    sql = "DELETE FROM funcionarios WHERE id = %s"
    try:
        cursor.executemany(sql, [(id,) for id in ids])
        conexao.commit()
    except Error as e:
        st.error(f"Erro ao remover funcionários: {e}")
    finally:
        cursor.close()
        conexao.close()

# Inicializar banco na primeira execução
base()

# Interface com Streamlit
st.title("Registo dos Funcionários")

# Formulário para adicionar funcionário
nome_input = st.text_input("Nome")
cargo_input = st.text_input("Cargo")
salario_input = st.number_input("Salário", min_value=0.0, format="%.2f")
if st.button("Adicionar Funcionário"):
    if nome_input.strip() == "" or cargo_input.strip() == "":
        st.error("Nome e Cargo não podem ser vazios!")
    elif salario_input <= 0:
        st.error("O salário deve ser maior que zero.")
    else:
        adicionar_funcionario(nome_input, cargo_input, salario_input)
        st.success("Funcionário registado com sucesso!")
        st.rerun()  # Recarrega a página para atualizar a lista

st.subheader("Funcionários Registados")
dados = obter_funcionarios()

# Filtro de Funcionários
search_name = st.text_input("Buscar por nome")
if search_name:
    dados = [f for f in dados if search_name.lower() in f[1].lower()]

# Lista para armazenar os IDs dos funcionários marcados para remoção
funcionarios_selecionados = []
if dados:
    for funcionario in dados:
        with st.expander(f"{funcionario[1]} - {funcionario[2]} - €{funcionario[3]:,.2f}"):
            # Criar duas colunas: uma para atualizar e outra para seleção para remoção
            col1, col2 = st.columns(2)
            with col1:
                novo_nome = st.text_input("Novo Nome", funcionario[1], key=f"nome_{funcionario[0]}")
                novo_cargo = st.text_input("Novo Cargo", funcionario[2], key=f"cargo_{funcionario[0]}")
                novo_salario = st.number_input("Novo Salário", min_value=0.0, 
                                               value=float(funcionario[3]), format="%.2f", key=f"salario_{funcionario[0]}")
                if st.button("Atualizar", key=f"atualizar_{funcionario[0]}"):
                    if novo_nome.strip() == "" or novo_cargo.strip() == "":
                        st.error("Nome e Cargo não podem ser vazios!")
                    elif novo_salario <= 0:
                        st.error("O salário deve ser maior que zero.")
                    else:
                        atualizar_funcionario(funcionario[0], novo_nome, novo_cargo, novo_salario)
                        st.success("Funcionário atualizado com sucesso!")
                        st.rerun()
            with col2:
                remover_checkbox = st.checkbox("Selecionar para remover", key=f"remover_{funcionario[0]}")
                if remover_checkbox:
                    funcionarios_selecionados.append(funcionario[0])
    if st.button("Remover Funcionários Selecionados"):
        if funcionarios_selecionados:
            remover_funcionarios_selecionados(funcionarios_selecionados)
            st.success(f"{len(funcionarios_selecionados)} funcionários removidos com sucesso!")
            st.rerun()
        else:
            st.warning("Selecione pelo menos um funcionário para remover.")
else:
    st.info("Nenhum funcionário registado na base de dados.")
