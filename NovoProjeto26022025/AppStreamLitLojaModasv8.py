import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import re
import os
from PIL import Image

# ------------------------------------------------
# 1. CONFIGURAÇÃO INICIAL E CRIAÇÃO DE TABELAS
# ------------------------------------------------

# Caminho da imagem padrão
NO_IMAGE_PATH = 'noimage.jpg'  # Certifica-te de que existe no mesmo diretório

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

# ------------------------------------------------
# 2. FUNÇÕES CRUD
# ------------------------------------------------

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

def eliminar_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conn.commit()
    cursor.close()
    conn.close()

def lista_produtos():
    """ Devolve todos os produtos da base de dados. """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

# ------------------------------------------------
# 3. GESTÃO DE LOGIN E WISHLIST (SESSION_STATE)
# ------------------------------------------------

def check_login(username, password):
    """ Exemplo simples de login. """
    # Podes substituir por algo mais complexo, p.ex. base de dados de utilizadores
    if username == "admin" and password == "123":
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.success("Login efetuado com sucesso!")
        
    else:
        st.error("Credenciais inválidas. Tente novamente.")

def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.success("Logout efetuado com sucesso!")


def init_session_state():
    """ Inicializa variáveis de sessão. """
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "wishlist" not in st.session_state:
        st.session_state["wishlist"] = []
    if "search" not in st.session_state:
        st.session_state["search"] = ""

def adicionar_wishlist(id_produto):
    """ Adiciona um produto à wishlist, se ainda não existir. """
    if id_produto not in st.session_state["wishlist"]:
        st.session_state["wishlist"].append(id_produto)
        st.success("Produto adicionado à Wishlist!")
    else:
        st.warning("Este produto já está na Wishlist!")

# ------------------------------------------------
# 4. PÁGINAS (HOME, PRODUTOS, ADICIONAR, EDITAR, ELIMINAR, LOGIN, WISHLIST, ETC.)
# ------------------------------------------------

def home_page():
    st.subheader("Bem-vindo à Loja de Moda!")
    st.write("Esta é uma plataforma para gerir os produtos da loja.")
    st.write("Use o menu lateral para navegar nas diferentes secções.")

def produtos_page():
    st.subheader("Produtos Disponíveis")

    # Obter todos os produtos
    produtos = lista_produtos()

    # Filtrar por pesquisa (se o utilizador escreveu algo no topo)
    if st.session_state["search"]:
        filtro = st.session_state["search"].lower()
        produtos = [p for p in produtos if filtro in p["nome"].lower() or filtro in p["descricao"].lower()]

    if produtos:
        # Mostrar produtos em grelha (3 por linha)
        cols_per_row = 3
        for i in range(0, len(produtos), cols_per_row):
            cols = st.columns(cols_per_row)
            for col, produto in zip(cols, produtos[i:i+cols_per_row]):
                with col:
                    st.image(produto['imagem'] if produto['imagem'] and os.path.exists(produto['imagem'])
                             else NO_IMAGE_PATH,
                             use_container_width=True)
                    st.write(f"**{produto['nome']}**")
                    st.write(f"Preço: €{produto['preco']:.2f}")
                    if st.button(f"Adicionar à Wishlist #{produto['id']}", key=f"wishlist_{produto['id']}"):
                        adicionar_wishlist(produto['id'])
    else:
        st.write("Não foram encontrados produtos ou a base de dados está vazia.")

def adicionar_page():
    st.subheader("Adicionar um Novo Produto")
    with st.form(key='produto_form_adicionar'):
        nome = st.text_input('Nome do Produto')
        descricao = st.text_area('Descrição do Produto')
        preco = st.number_input('Preço', min_value=0.01, step=0.01)
        imagem_file = st.file_uploader("Carregar Imagem do Produto", type=["jpg", "jpeg", "png"])
        
        submit_button = st.form_submit_button(label='Inserir o Produto')

        if submit_button:
            # Validações simples
            if not nome.strip():
                st.error('Por favor, insira um nome válido para o produto.')
            elif nome.isdigit():
                st.error('O nome do produto não pode conter apenas números.')
            elif not re.search(r'^[a-zA-Z0-9\s]+$', nome):
                st.error('Por favor, insira um nome válido para o produto (sem símbolos especiais).')
            elif descricao.strip() == "":
                st.error('A descrição não pode estar vazia.')
            elif not re.search(r'^[a-zA-Z0-9\s]+$', descricao):
                st.error('A descrição não pode ter símbolos especiais.')
            elif preco <= 0:
                st.error('O preço deve ser maior que zero.')
            else:
                # Processar imagem
                if imagem_file is not None:
                    imagem_nome = imagem_file.name
                    imagem_path = os.path.join("images", imagem_nome)
                    with open(imagem_path, "wb") as f:
                        f.write(imagem_file.getbuffer())
                else:
                    imagem_path = NO_IMAGE_PATH
                
                adiciona_produto(nome, descricao, preco, imagem_path)
                st.success(f'O produto "{nome}" foi registado com sucesso!')

def editar_page():
    st.subheader("Editar Produto")

    produtos = lista_produtos()
    if not produtos:
        st.write("Não há produtos para editar.")
        return
    
    produto_selecionado = st.selectbox(
        "Escolha o Produto a Editar",
        [f"{p['id']} - {p['nome']}" for p in produtos]
    )

    if produto_selecionado:
        id_produto_selecionado = int(produto_selecionado.split(" - ")[0])
        produto = next(p for p in produtos if p['id'] == id_produto_selecionado)

        with st.form(key=f'editar_form_{id_produto_selecionado}'):
            nome = st.text_input('Nome do Produto', produto['nome'])
            descricao = st.text_area('Descrição do Produto', produto['descricao'])
            preco = st.number_input('Preço', min_value=0.01, step=0.01, value=float(produto['preco']))
            imagem_file = st.file_uploader("Carregar Nova Imagem do Produto", type=["jpg", "jpeg", "png"])
            
            submit_button = st.form_submit_button(label='Atualizar Produto')

            if submit_button:
                # Validações
                if not nome.strip():
                    st.error('Por favor, insira um nome válido para o produto.')
                elif nome.isdigit():
                    st.error('O nome do produto não pode conter apenas números.')
                elif not re.search(r'^[a-zA-Z0-9\s]+$', nome):
                    st.error('Por favor, insira um nome válido para o produto.')
                elif descricao.strip() == "":
                    st.error('A descrição não pode estar vazia.')
                elif not re.search(r'^[a-zA-Z0-9\s]+$', descricao):
                    st.error('A descrição não pode ter símbolos especiais.')
                elif preco <= 0:
                    st.error('O preço deve ser maior que zero.')
                else:
                    # Se houve upload de imagem, substitui
                    if imagem_file is not None:
                        imagem_nome = imagem_file.name
                        imagem_path = os.path.join("images", imagem_nome)
                        with open(imagem_path, "wb") as f:
                            f.write(imagem_file.getbuffer())
                    else:
                        imagem_path = produto['imagem']
                    
                    atualizar_produto(id_produto_selecionado, nome, descricao, preco, imagem_path)
                    st.success(f'Produto "{nome}" atualizado com sucesso!')

def eliminar_page():
    st.subheader("Eliminar Produto")

    produtos = lista_produtos()
    if not produtos:
        st.write("Não há produtos para eliminar.")
        return

    produto_selecionado = st.selectbox(
        "Escolha o Produto a Eliminar",
        [f"{p['id']} - {p['nome']}" for p in produtos]
    )

    if produto_selecionado:
        id_produto_selecionado = int(produto_selecionado.split(" - ")[0])
        produto = next(p for p in produtos if p['id'] == id_produto_selecionado)

        confirm = st.checkbox(f"Tem a certeza que deseja excluir o produto {produto['nome']}?")
        if confirm:
            if st.button(f"Eliminar {produto['nome']}"):
                eliminar_produto(id_produto_selecionado)
                st.success(f"Produto {produto['nome']} eliminado com sucesso!")

def wishlist_page():
    st.subheader("A sua Wishlist")
    if not st.session_state["wishlist"]:
        st.write("Não há produtos na Wishlist.")
        return
    
    # Obter todos os produtos
    produtos = lista_produtos()
    # Filtrar só os da wishlist
    produtos_wishlist = [p for p in produtos if p['id'] in st.session_state["wishlist"]]

    if produtos_wishlist:
        cols_per_row = 3
        for i in range(0, len(produtos_wishlist), cols_per_row):
            cols = st.columns(cols_per_row)
            for col, produto in zip(cols, produtos_wishlist[i:i+cols_per_row]):
                with col:
                    st.image(produto['imagem'] if produto['imagem'] and os.path.exists(produto['imagem'])
                             else NO_IMAGE_PATH,
                             use_container_width=True)
                    st.write(f"**{produto['nome']}**")
                    st.write(f"Preço: €{produto['preco']:.2f}")
                    # Botão para remover da wishlist
                    if st.button(f"Remover #{produto['id']}", key=f"remove_wishlist_{produto['id']}"):
                        st.session_state["wishlist"].remove(produto['id'])
    else:
        st.write("A Wishlist está vazia.")

def login_page():
    st.subheader("Login")
    if st.session_state["logged_in"]:
        st.write(f"Já estás autenticado como: {st.session_state['username']}")
        if st.button("Logout"):
            logout()
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Iniciar Sessão"):
            check_login(username, password)

# ------------------------------------------------
# 5. SEÇÕES EXTRA (PLACEHOLDERS)
# ------------------------------------------------

def descontos_page():
    st.subheader("Descontos")
    st.write("Exemplo de página de descontos. (Em desenvolvimento)")

def mais_vendidos_page():
    st.subheader("Mais Vendidos")
    st.write("Exemplo de página de produtos mais vendidos. (Em desenvolvimento)")

def marcas_page():
    st.subheader("Marcas")
    st.write("Exemplo de página para listar marcas. (Em desenvolvimento)")

def suporte_page():
    st.subheader("Suporte")
    st.write("Exemplo de página de suporte ao cliente. (Em desenvolvimento)")

def entregas_page():
    st.subheader("Entregas")
    st.write("Exemplo de página de entregas. (Em desenvolvimento)")

# ------------------------------------------------
# 6. MAIN (EXECUÇÃO PRINCIPAL DO STREAMLIT)
# ------------------------------------------------

def main():
    # Criar base de dados e tabela se não existirem
    cria_tabela()
    # Inicializar variáveis de sessão
    init_session_state()

    # CSS Personalizado
    st.markdown("""
    <style>
    /* Barra de título */
    .title-bar {
        background-color: #4CAF50;
        padding: 10px;
        text-align: center;
        font-size: 30px;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    /* Fonte geral */
    .stApp {
        font-family: Arial, sans-serif;
    }
    /* Ajustar cor de fundo do menu lateral */
    .css-1cpxqw2 {
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

    # Título final da página principal
    st.title("Gestão de Produtos - Loja de Moda")
    
    # Barra de título no topo
    st.markdown('<div class="title-bar">Loja de Moda</div>', unsafe_allow_html=True)

    # ------------------------------------------------
    # Barra de Topo (Pesquisa, Secções, Wishlist)
    # ------------------------------------------------
    col1, col2, col3 = st.columns([3, 4, 1])

    with col1:
        # Barra de pesquisa
        st.session_state["search"] = st.text_input("Pesquisar", value=st.session_state["search"], placeholder="Pesquisar produtos...")

    with col2:
        # Links rápidos (Descontos, Mais Vendidos, Marcas, Suporte, Entregas)
        st.markdown("""
        **[Descontos](#) | [Mais Vendidos](#) | [Marcas](#) | [Suporte](#) | [Entregas](#)**
        """)
    with col3:
        # Botão Wishlist
        if st.button("Wishlist"):
            st.session_state["page"] = "Wishlist"

    # ------------------------------------------------
    # Menu Lateral (usando streamlit-option_menu)
    # ------------------------------------------------
    with st.sidebar:
        escolha = option_menu(
            "Menu",
            ["Home", "Produtos", "Adicionar", "Editar", "Eliminar", "Wishlist", "Login/Logout"],
            icons=["house", "cart", "plus", "pencil", "trash", "heart", "person"],
            menu_icon="list",
            default_index=0
        )

    # Lógica para abrir a página consoante a escolha
    if escolha == "Home":
        home_page()
    elif escolha == "Produtos":
        produtos_page()
    elif escolha == "Adicionar":
        if st.session_state["logged_in"]:
            adicionar_page()
        else:
            st.warning("Precisas de estar autenticado para adicionar produtos.")
    elif escolha == "Editar":
        if st.session_state["logged_in"]:
            editar_page()
        else:
            st.warning("Precisas de estar autenticado para editar produtos.")
    elif escolha == "Eliminar":
        if st.session_state["logged_in"]:
            eliminar_page()
        else:
            st.warning("Precisas de estar autenticado para eliminar produtos.")
    elif escolha == "Wishlist":
        wishlist_page()
    elif escolha == "Login/Logout":
        login_page()

    

# ------------------------------------------------
# EXECUTAR A APLICAÇÃO
# ------------------------------------------------
if __name__ == "__main__":
    main()
