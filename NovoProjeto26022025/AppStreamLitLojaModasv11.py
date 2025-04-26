import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import os
from PIL import Image, UnidentifiedImageError
import bcrypt
from io import BytesIO

# ------------------------------------------------
# 1. CONFIGURAÇÃO INICIAL E CRIAÇÃO DE TABELAS
# ------------------------------------------------

NO_IMAGE_PATH = 'noimage.jpg'
MAX_IMAGE_SIZE_MB = 5  # Tamanho máximo de 5MB para imagens

# Criar diretórios necessários
os.makedirs("images", exist_ok=True)

# Configuração da ligação ao MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'loja_modas'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        st.error(f"Erro ao conectar à base de dados: {err}")
        return None

def cria_base_de_dados():
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
    
    # Cria o base de dados se não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS loja_modas")
    conn.commit()
    cursor.close()
    conn.close()

def criar_admin_se_nao_existir():
    # Verifica se o administrador já existe
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utilizadores WHERE is_admin = TRUE")
    admin = cursor.fetchone()

    # Se não existir administrador, cria um
    if admin is None:
        sucesso = criar_utilizador('admin', 'adminpassword', True)  # Senha do admin
        if sucesso:
            st.session_state['admin_criado'] = True  # Marca que o admin foi criado
    cursor.close()
    conn.close()

def cria_tabelas():
    # Criação do base de dados, se necessário
    cria_base_de_dados()

    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        # Tabela de utilizadores
        cursor.execute('''CREATE TABLE IF NOT EXISTS utilizadores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                is_admin BOOLEAN DEFAULT FALSE
            )''')
        
        # Tabela de produtos
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                descricao TEXT,
                preco DECIMAL(10,2) NOT NULL,
                categoria VARCHAR(100),
                imagem VARCHAR(255),
                stock INT DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        conn.commit()
    except mysql.connector.Error as err:
        st.error(f"Erro na criação das tabelas: {err}")
    finally:
        cursor.close()
        conn.close()

# ------------------------------------------------
# 2. SEGURANÇA E AUTENTICAÇÃO
# ------------------------------------------------

def verificar_login(username, password):
    """Função para verificar as credenciais de login do utilizador."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM utilizadores WHERE username = %s", (username,))
        utilizador = cursor.fetchone()
        
        if utilizador and bcrypt.checkpw(password.encode('utf-8'), utilizador['password_hash'].encode('utf-8')):
            # Se o login for bem-sucedido, armazena o estado da sessão
            st.session_state.update({
                "logged_in": True,
                "user_id": utilizador['id'],
                "username": utilizador['username'],
                "is_admin": utilizador['is_admin']  # Armazena o status de admin diretamente na sessão
            })
            return True
        return False
    except mysql.connector.Error as err:
        st.error(f"Erro ao verificar login: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def pagina_login():
    """Página de login para o utilizador inserir as credenciais."""
    with st.form("login_form"):
        # Recebe o nome de utilizador e a senha do formulário
        username = st.text_input("Nome do Utilizador")
        password = st.text_input("Senha", type="password")
        
        # Botão para enviar e validar as credenciais
        if st.form_submit_button("Login"):
            if verificar_login(username, password):
                st.success(f"Bem-vindo, {username}!")
                # Redefine a página para o "Home" após o login bem-sucedido
                st.session_state.pagina = 'home'  
            else:
                st.error("Credenciais inválidas")

# ------------------------------------------------
# 5. REGISTO DO UTILIZADOR
# ------------------------------------------------

def criar_utilizador(username, password, is_admin=False):
    # Verifica se o nome de utilizador já existe na base de dados
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilizadores WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            st.error(f"O Utilizador {username} já existe!")
            return False  # Se já existe, não cria o utilizador
        
        # Se não existir, cria o utilizador
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        cursor.execute(
            "INSERT INTO utilizadores (username, password_hash, is_admin) VALUES (%s, %s, %s)",
            (username, password_hash.decode('utf-8'), is_admin)
        )
        conn.commit()
        st.success(f"O Utilizador {username} foi criado com sucesso!")
        return True
    except mysql.connector.Error as err:
        st.error(f"Erro ao criar o utilizador: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def dashboard_admin():
    st.header("Dashboard do Administrador")
    st.subheader("Adicionar Novo Produto")

    with st.form("add_product_form"):
        nome = st.text_input("Nome do Produto")
        descricao = st.text_area("Descrição")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        categoria = st.text_input("Categoria")
        stock = st.number_input("Quantidade em stock", min_value=0, step=1)
        imagem = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

        if st.form_submit_button("Adicionar Produto"):
            if imagem is not None:
                # Salva a imagem na pasta "images"
                img_path = os.path.join("images", imagem.name)
                with open(img_path, "wb") as f:
                    f.write(imagem.getbuffer())

                st.success("Produto adicionado com sucesso.")
            else:
                st.error("A Imagem é obrigatória.")

    st.subheader("Produtos Registados")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    for produto in produtos:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(produto['imagem'] if os.path.exists(produto['imagem']) else NO_IMAGE_PATH, width=100)
        with col2:
            st.markdown(f"**{produto['nome']}**")
            st.write(f"Preço: €{produto['preco']:.2f}")
            st.write(f"Categoria: {produto['categoria']}")
            st.write(f"Stock: {produto['stock']}")
        with col3:
            if st.button(f"Editar {produto['nome']}", key=f"edit_{produto['id']}"):
                st.write("Editar produto")
            if st.button(f"Apagar {produto['nome']}", key=f"delete_{produto['id']}"):
                st.write("Apagar produto")

def main():
    cria_tabelas()

    # Garantir que o admin seja criado uma única vez
    if 'admin_criado' not in st.session_state:
        criar_admin_se_nao_existir()  # Criação do admin
        # Não mostra mais mensagens de criação de admin
        st.session_state['admin_criado'] = True  # Marca que o admin foi criado
    
    if 'pagina' not in st.session_state:
        st.session_state.pagina = 'login'

    # Navegação principal
    if not st.session_state.get('logged_in'):
        pagina_login()
        return

    # Menu principal após login
    with st.sidebar:
        escolha = option_menu(
            "Menu Principal",
            ["Home", "Produtos", "Wishlist", "Perfil"],
            icons=["house", "cart", "heart", "person"],
            menu_icon="list"
        )
        
        if st.button("Logout"):
            # Limpar estado da sessão e voltar à página de login
            st.session_state.clear()  # Limpa o estado da sessão
            st.session_state.pagina = 'login'  # Redireciona para a página de login
            return  # Sai da execução do main

    # Navegação para o Dashboard se o usuário for admin
    if st.session_state.get("is_admin") and escolha == "Produtos":
        st.session_state.pagina = "dashboard"  # Definindo qual página será exibida
        dashboard_admin()
    elif st.session_state.pagina == 'home':
        # Exibir a página inicial (exemplo)
        st.header("Bem-vindo à Loja de Modas")
        # A lógica para exibir os produtos seria aqui
    elif st.session_state.pagina == 'login':
        pagina_login()

if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado diretamente
