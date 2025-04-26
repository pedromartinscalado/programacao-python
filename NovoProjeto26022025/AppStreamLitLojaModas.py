import streamlit as st
import mysql.connector
import os

# Configuração da ligação ao MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'loja_modas'
}

# Função para estabelecer a ligação ao MySQL
def get_db_connection():
    conn = mysql.connector.connect(host='localhost', user='root', password='')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS loja_modas")
    cursor.close()
    conn.close()
    conn = mysql.connector.connect(**db_config)
    return conn

# Função para criar a tabela caso não exista
def cria_tabela():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            descricao TEXT,
            preco DECIMAL(10,2) NOT NULL,
            imagem VARCHAR(255)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Função para adicionar um novo produto à base de dados
def adiciona_produto(nome, descricao, preco, imagem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, imagem) VALUES (%s, %s, %s, %s)",
        (nome, descricao, preco, imagem)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Função para exibir os produtos registados
def mostra_produtos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    if produtos:
        for produto in produtos:
            st.write(f"**Nome:** {produto['nome']}")
            st.write(f"**Descrição:** {produto['descricao']}")
            st.write(f"**Preço:** €{produto['preco']:.2f}")
            
            if produto['imagem'] and os.path.exists(produto['imagem']):
                st.image(produto['imagem'], caption=f"Imagem de {produto['nome']}", use_container_width=True)
            else:
                st.write("Imagem não disponível")
            
            st.write("------")
    else:
        st.write("Não há produtos registados na base de dados.")

# Criar a base de dados e a tabela ao iniciar o programa
cria_tabela()

# Interface do Streamlit
st.title('Registo de Produtos - Loja de Moda')

# Formulário para adicionar um novo produto
with st.form(key='produto_form'):
    nome = st.text_input('Nome do Produto')
    descricao = st.text_area('Descrição do Produto')
    preco = st.number_input('Preço', min_value=0.01, step=0.01)
    imagem = st.text_input('Caminho da Imagem')  # Caminho da imagem
    
    submit_button = st.form_submit_button(label='Inserir o Produto')

    if submit_button:
        if nome.strip() and preco > 0:
            adiciona_produto(nome, descricao, preco, imagem)
            st.success('Produto registado com sucesso!')
            st.rerun()  # Atualiza a página após inserir
        else:
            st.error('Por favor, preenche todos os campos obrigatórios.')

# Mostrar os produtos registados
st.subheader('Produtos Registados:')
mostra_produtos()


