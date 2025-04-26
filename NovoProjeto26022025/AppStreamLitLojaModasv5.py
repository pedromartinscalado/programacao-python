import streamlit as st
import mysql.connector
import os
from PIL import Image
import io

# Caminho da imagem padrão
NO_IMAGE_PATH = 'noimage.jpg'  # Certifique-se de ter a imagem no caminho correto

# Criação do diretório de imagens, se não existir
if not os.path.exists("images"):
    os.makedirs("images")

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

# Função para atualizar um produto existente
def atualizar_produto(id_produto, nome, descricao, preco, imagem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s, preco = %s, imagem = %s WHERE id = %s",
        (nome, descricao, preco, imagem, id_produto)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Função para eliminar um produto
def eliminar_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
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
            
            # Verificação da imagem, se não existir ou não for válida, usa a imagem noimage.jpg
            if produto['imagem'] and os.path.exists(produto['imagem']):
                st.image(produto['imagem'], caption=f"Imagem de {produto['nome']}", use_container_width=True)
            else:
                st.image(NO_IMAGE_PATH, caption="Imagem não disponível", use_container_width=True)
            
            st.write("------")
    else:
        st.write("Não há produtos registados na base de dados.")

# Criar a base de dados e a tabela ao iniciar o programa
cria_tabela()

# Interface do Streamlit
st.title('Gestão de Produtos - Loja de Moda')

# Abas para CRUD
abas = ["Adicionar Produto", "Mostrar Produtos", "Editar Produto", "Eliminar Produto"]
aba_selecionada = st.sidebar.radio("Escolha uma opção", abas)

# Função para adicionar produto
if aba_selecionada == "Adicionar Produto":
    st.subheader("Adicionar um Novo Produto")
    
    with st.form(key='produto_form_adicionar'):
        nome = st.text_input('Nome do Produto')
        descricao = st.text_area('Descrição do Produto')
        preco = st.number_input('Preço', min_value=0.01, step=0.01)
        
        # Upload da imagem
        imagem_file = st.file_uploader("Carregar Imagem do Produto", type=["jpg", "jpeg", "png"])

        # Se o usuário carregar uma imagem, convertemos para um caminho ou nome de arquivo
        imagem = None
        if imagem_file is not None:
            imagem = f"images/{imagem_file.name}"
            with open(imagem, "wb") as f:
                f.write(imagem_file.getbuffer())
        
        # Botão de submit dentro do formulário
        submit_button = st.form_submit_button(label='Inserir o Produto')

        # Validação dos campos obrigatórios
        if submit_button:
            if nome.strip() and descricao.strip() and preco > 0:
                if imagem:
                    # Adiciona o produto com a imagem carregada
                    adiciona_produto(nome, descricao, preco, imagem)
                else:
                    # Se não houver imagem, será adicionada a imagem default
                    adiciona_produto(nome, descricao, preco, NO_IMAGE_PATH)
                
                # Exibe a mensagem de sucesso
                st.success(f'O produto "{nome}" foi registrado com sucesso!')
            else:
                st.error('Por favor, preencha todos os campos obrigatórios.')

# Função para mostrar os produtos registados
elif aba_selecionada == "Mostrar Produtos":
    st.subheader("Produtos Registados: ")
    mostra_produtos()  # Exibe os produtos

# Função para editar produto
elif aba_selecionada == "Editar Produto":
    st.subheader("Editar Produto")

    # Seleção do produto a editar
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    if produtos:
        produto_selecionado = st.selectbox("Escolha o Produto a Editar", [f"{produto['id']} - {produto['nome']}" for produto in produtos])

        if produto_selecionado:
            id_produto_selecionado = int(produto_selecionado.split(" - ")[0])
            produto = next(p for p in produtos if p['id'] == id_produto_selecionado)
            nome_atual = produto['nome']
            descricao_atual = produto['descricao']
            preco_atual = float(produto['preco'])  # Converte para float
            imagem_atual = produto['imagem']

            with st.form(key=f'editar_form_{id_produto_selecionado}'):
                nome = st.text_input('Nome do Produto', nome_atual)
                descricao = st.text_area('Descrição do Produto', descricao_atual)
                preco = st.number_input('Preço', min_value=0.01, step=0.01, value=preco_atual)
                
                # Upload da nova imagem
                imagem_file = st.file_uploader("Carregar Nova Imagem do Produto", type=["jpg", "jpeg", "png"])

                # Verificar se o usuário fez upload de uma nova imagem
                imagem = None
                if imagem_file is not None:
                    imagem = f"images/{imagem_file.name}"
                    with open(imagem, "wb") as f:
                        f.write(imagem_file.getbuffer())
                else:
                    imagem = imagem_atual  # Mantém a imagem atual caso não tenha sido feito upload

                submit_button = st.form_submit_button(label='Atualizar Produto')

                if submit_button:
                    if nome.strip() and preco > 0:
                        atualizar_produto(id_produto_selecionado, nome, descricao, preco, imagem)
                        st.success(f'Produto "{nome}" atualizado com sucesso!')
                    else:
                        st.error('Por favor, preencha todos os campos obrigatórios.')

    else:
        st.write("Não há produtos para editar.")

# Função para eliminar produto
elif aba_selecionada == "Eliminar Produto":
    st.subheader("Eliminar Produto")
    
    # Seleção do produto a eliminar
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    if produtos:
        produto_selecionado = st.selectbox("Escolha o Produto a Eliminar", [f"{produto['id']} - {produto['nome']}" for produto in produtos])

        if produto_selecionado:
            id_produto_selecionado = int(produto_selecionado.split(" - ")[0])
            produto = next(p for p in produtos if p['id'] == id_produto_selecionado)

            confirm = st.checkbox(f"Tem certeza que deseja excluir o produto {produto['nome']}?", key="confirm_delete")
            if confirm:
                if st.button(f"Eliminar {produto['nome']}"):
                    eliminar_produto(id_produto_selecionado)
                    st.success(f"Produto {produto['nome']} eliminado com sucesso!")
                else:
                    st.warning(f"Produto {produto['nome']} não foi excluído.")
    else:
        st.write("Não há produtos para eliminar.")
