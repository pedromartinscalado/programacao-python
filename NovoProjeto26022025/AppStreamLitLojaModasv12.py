import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import re
import os
import bcrypt
from PIL import Image

# ------------------------------------------------
# 1. CONFIGURAÇÃO INICIAL E CRIAÇÃO DE TABELAS
# ------------------------------------------------

# Caminho da imagem padrão (certifica-te de que o ficheiro existe)
NO_IMAGE_PATH = 'noimage.jpg'

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

# Função para estabelecer a ligação ao MySQL com tratamento de exceções
def get_db_connection():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS loja_modas")
        cursor.close()
        conn.close()
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        st.error(f"Erro ao conectar à base de dados: {err}")
        return None

# Função para criar as tabelas caso não existam
def cria_tabelas():
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        
        # Tabela de produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                descricao TEXT,
                preco DECIMAL(10,2) NOT NULL,
                imagem VARCHAR(255)
            )
        ''')
        
        # Tabela de utilizadores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS utilizadores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                nome VARCHAR(100),
                email VARCHAR(100),
                is_admin BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Inserir utilizador admin se não existir
        cursor.execute("SELECT * FROM utilizadores WHERE username = 'admin'")
        if not cursor.fetchone():
            # FAZER HASH DA PASSWORD ADMIN COM BCRYPT ANTES DE INSERIR
                admin_password = '123' # Password inicial do admin
                hashed_admin_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())

                cursor.execute(
                    "INSERT INTO utilizadores (username, password_hash, nome, email, is_admin) VALUES (%s, %s, %s, %s, %s)",
                    ('admin', hashed_admin_password, 'Administrador', 'admin@exemplo.com', True)
                )   
        
        conn.commit()
    except mysql.connector.Error as err:
        st.error(f"Erro na criação das tabelas: {err}")
    finally:
        cursor.close()
        conn.close()

# ------------------------------------------------
# 2. FUNÇÕES CRUD COM TRATAMENTO DE ERROS
# ------------------------------------------------

def adiciona_produto(nome, descricao, preco, imagem):
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, descricao, preco, imagem) VALUES (%s, %s, %s, %s)",
            (nome, descricao, preco, imagem)
        )
        conn.commit()
        st.success("Produto adicionado com sucesso!")
    except mysql.connector.Error as err:
        st.error(f"Erro ao adicionar produto: {err}")
    finally:
        cursor.close()
        conn.close()

def atualizar_produto(id_produto, nome, descricao, preco, imagem):
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET nome = %s, descricao = %s, preco = %s, imagem = %s WHERE id = %s",
            (nome, descricao, preco, imagem, id_produto)
        )
        conn.commit()
        st.success("Produto atualizado com sucesso!")
    except mysql.connector.Error as err:
        st.error(f"Erro ao atualizar produto: {err}")
    finally:
        cursor.close()
        conn.close()

def eliminar_produto(id_produto):
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conn.commit()
        st.success("Produto eliminado com sucesso!")
    except mysql.connector.Error as err:
        st.error(f"Erro ao eliminar produto: {err}")
    finally:
        cursor.close()
        conn.close()

def lista_produtos():
    """ Devolve todos os produtos da base de dados. """
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        return produtos
    except mysql.connector.Error as err:
        st.error(f"Erro ao listar produtos: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

# ------------------------------------------------
# 3. FUNÇÕES DE GESTÃO DE UTILIZADORES
# ------------------------------------------------

def regista_utilizador(username, password_hash, nome, email, is_admin=False):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        # Verificar se o utilizador já existe (mantém-se igual)
        cursor.execute("SELECT * FROM utilizadores WHERE username = %s", (username,))
        if cursor.fetchone():
            st.error("Este nome de utilizador já existe!")
            return False

        # FAZER HASH DA password_hash COM BCRYPT
        hashed_password_hash = bcrypt.hashpw(password_hash.encode('utf-8'), bcrypt.gensalt()) # HASH DA password_hash

        cursor.execute(
            "INSERT INTO utilizadores (username, password_hash, nome, email, is_admin) VALUES (%s, %s, %s, %s, %s)", # USAR password_hash
            (username, hashed_password_hash, nome, email, is_admin) # GUARDAR password_hash HASHED
        )
        conn.commit()
        st.success("Utilizador registado com sucesso!")
        return True
    except mysql.connector.Error as err:
        st.error(f"Erro ao registar utilizador: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def check_login(username, password_hash):
    """Verifica as credenciais na base de dados usando bcrypt."""
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM utilizadores WHERE username = %s", (username,)) # REMOVEU 'AND password_hash = %s'
        user = cursor.fetchone()
        if user:
            # VERIFICAR password_hash COM BCRYPT
            if bcrypt.checkpw(password_hash.encode('utf-8'), user['password_hash'].encode('utf-8')): # USAR password_hash
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["user_id"] = user["id"]
                st.session_state["is_admin"] = user["is_admin"]
                st.success(f"Bem-vindo, {username}!")
                return True
            else:
                st.error("password_hash inválida. Tente novamente.") # MENSAGEM DE password_hash INCORRETA
                return False
        else:
            st.error("Utilizador não encontrado. Verifique o nome de utilizador.") # MENSAGEM DE USERNAME INCORRETO
            return False
    except mysql.connector.Error as err:
        st.error(f"Erro ao verificar login: {err}")
        return False
    finally:
        cursor.close()
        conn.close()


def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["user_id"] = None
    st.session_state["is_admin"] = False
    st.success("Logout efetuado com sucesso!")

def lista_utilizadores():
    """Lista todos os utilizadores da base de dados."""
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, username, nome, email, is_admin FROM utilizadores")
        utilizadores = cursor.fetchall()
        return utilizadores
    except mysql.connector.Error as err:
        st.error(f"Erro ao listar utilizadores: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def eliminar_utilizador(id_utilizador):
    """Elimina um utilizador da base de dados."""
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM utilizadores WHERE id = %s", (id_utilizador,))
        conn.commit()
        st.success("Utilizador eliminado com sucesso!")
    except mysql.connector.Error as err:
        st.error(f"Erro ao eliminar utilizador: {err}")
    finally:
        cursor.close()
        conn.close()

# ------------------------------------------------
# 4. GESTÃO DE WISHLIST E SESSÃO
# ------------------------------------------------

def init_session_state():
    """Inicializa variáveis de sessão."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = None
    if "is_admin" not in st.session_state:
        st.session_state["is_admin"] = False
    if "wishlist" not in st.session_state:
        st.session_state["wishlist"] = []
    if "search" not in st.session_state:
        st.session_state["search"] = ""
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

def adicionar_wishlist(id_produto):
    """Adiciona um produto à wishlist, se ainda não existir."""
    if id_produto not in st.session_state["wishlist"]:
        st.session_state["wishlist"].append(id_produto)
        st.success("Produto adicionado à Wishlist!")
    else:
        st.warning("Este produto já está na Wishlist!")

# Função para sanitizar o nome do ficheiro (removendo caracteres indesejados)
def sanitize_filename(filename):
    return re.sub(r'[^\w\.-]', '_', filename)

# ------------------------------------------------
# 5. PÁGINAS DA APLICAÇÃO
# ------------------------------------------------

def home_page():
    st.subheader("Bem-vindo à Loja de Moda!")
    st.write("Esta é uma plataforma para gerir os produtos da loja.")
    st.write("Use o menu lateral para navegar nas diferentes secções.")
    
    # Destaque para alguns produtos na página inicial
    st.subheader("Produtos em Destaque")
    produtos = lista_produtos()
    if produtos:
        # Mostrar apenas até 3 produtos em destaque
        produtos_destaque = produtos[:min(3, len(produtos))]
        cols = st.columns(len(produtos_destaque))
        for i, produto in enumerate(produtos_destaque):
            with cols[i]:
                st.image(produto['imagem'] if produto['imagem'] and os.path.exists(produto['imagem'])
                         else NO_IMAGE_PATH,
                         use_container_width=True)
                st.write(f"**{produto['nome']}**")
                st.write(f"Preço: €{produto['preco']:.2f}")
    else:
        st.info("Não há produtos disponíveis para mostrar.")

def produtos_page():
    st.subheader("Produtos Disponíveis")
    produtos = lista_produtos()
    # Filtrar por pesquisa
    if st.session_state["search"]:
        filtro = st.session_state["search"].lower()
        produtos = [p for p in produtos if filtro in p["nome"].lower() or filtro in p["descricao"].lower()]
    if produtos:
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
        st.info("Não foram encontrados produtos ou a base de dados está vazia.")

def adicionar_page():
    st.subheader("Adicionar um Novo Produto")
    with st.form(key='produto_form_adicionar'):
        nome = st.text_input('Nome do Produto')
        descricao = st.text_area('Descrição do Produto')
        preco = st.number_input('Preço', min_value=0.01, step=0.01)
        imagem_file = st.file_uploader("Carregar Imagem do Produto", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Inserir o Produto')
        
        # Validação usando regex que permite caracteres acentuados
        pattern = r'^[\wÀ-ÿ\s]+$'
        if submit_button:
            if not nome.strip():
                st.error('Por favor, insira um nome válido para o produto.')
            elif nome.isdigit():
                st.error('O nome do produto não pode conter apenas números.')
            elif not re.match(pattern, nome):
                st.error('O nome do produto contém caracteres inválidos.')
            elif descricao.strip() == "":
                st.error('A descrição não pode estar vazia.')
            elif not re.match(pattern, descricao):
                st.error('A descrição contém caracteres inválidos.')
            elif preco <= 0:
                st.error('O preço deve ser maior que zero.')
            else:
                # Processar e sanitizar a imagem
                if imagem_file is not None:
                    imagem_nome = sanitize_filename(imagem_file.name)
                    imagem_path = os.path.join("images", imagem_nome)
                    with open(imagem_path, "wb") as f:
                        f.write(imagem_file.getbuffer())
                else:
                    imagem_path = NO_IMAGE_PATH
                adiciona_produto(nome, descricao, preco, imagem_path)

def editar_page():
    st.subheader("Editar Produto")
    produtos = lista_produtos()
    if not produtos:
        st.info("Não há produtos para editar.")
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
            pattern = r'^[\wÀ-ÿ\s]+$'
            if submit_button:
                if not nome.strip():
                    st.error('Por favor, insira um nome válido para o produto.')
                elif nome.isdigit():
                    st.error('O nome do produto não pode conter apenas números.')
                elif not re.match(pattern, nome):
                    st.error('O nome contém caracteres inválidos.')
                elif descricao.strip() == "":
                    st.error('A descrição não pode estar vazia.')
                elif not re.match(pattern, descricao):
                    st.error('A descrição contém caracteres inválidos.')
                elif preco <= 0:
                    st.error('O preço deve ser maior que zero.')
                else:
                    if imagem_file is not None:
                        imagem_nome = sanitize_filename(imagem_file.name)
                        imagem_path = os.path.join("images", imagem_nome)
                        with open(imagem_path, "wb") as f:
                            f.write(imagem_file.getbuffer())
                    else:
                        imagem_path = produto['imagem']
                    atualizar_produto(id_produto_selecionado, nome, descricao, preco, imagem_path)

def eliminar_page():
    st.subheader("Eliminar Produto")
    produtos = lista_produtos()
    if not produtos:
        st.info("Não há produtos para eliminar.")
        return
    produto_selecionado = st.selectbox(
        "Escolha o Produto a Eliminar",
        [f"{p['id']} - {p['nome']}" for p in produtos]
    )
    if produto_selecionado:
        id_produto_selecionado = int(produto_selecionado.split(" - ")[0])
        produto = next(p for p in produtos if p['id'] == id_produto_selecionado)
        confirm = st.checkbox(f"Tem a certeza que deseja excluir o produto {produto['nome']}?")
        if confirm and st.button(f"Eliminar {produto['nome']}"):
            eliminar_produto(id_produto_selecionado)

def wishlist_page():
    st.subheader("A sua Wishlist")
    if not st.session_state["wishlist"]:
        st.info("Não há produtos na Wishlist.")
        return
    produtos = lista_produtos()
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
                    if st.button(f"Remover #{produto['id']}", key=f"remove_wishlist_{produto['id']}"):
                        st.session_state["wishlist"].remove(produto['id'])
    else:
        st.info("A Wishlist está vazia.")

def login_page():
    st.subheader("Área de Utilizador")
    
    if st.session_state["logged_in"]:
        st.write(f"Utilizador autenticado: **{st.session_state['username']}**")
        
        if st.session_state["is_admin"]:
            st.success("Acesso de Administrador")
            
            # Tabs para diferentes funções de administrador
            tab1, tab2 = st.tabs(["Perfil", "Gestão de Utilizadores"])
            
            with tab1:
                st.subheader("Informações do Perfil")
                st.write("Aqui poderás alterar as tuas informações pessoais (funcionalidade em desenvolvimento)")
                
                if st.button("Logout", key="btn_logout_admin"):
                    logout()
                    st.rerun()
            
            with tab2:
                st.subheader("Gerir Utilizadores")
                utilizadores = lista_utilizadores()
                if utilizadores:
                    st.write(f"Total de utilizadores: {len(utilizadores)}")
                    
                    # Listagem de utilizadores em tabela
                    user_data = []
                    for u in utilizadores:
                        user_data.append({
                            "ID": u['id'],
                            "Username": u['username'],
                            "Nome": u['nome'] if u['nome'] else "-",
                            "Email": u['email'] if u['email'] else "-",
                            "Tipo": "Admin" if u['is_admin'] else "Regular"
                        })
                    
                    st.table(user_data)
                    
                    # Formulário para eliminar utilizador
                    st.write("---")
                    st.subheader("Eliminar Utilizador")
                    user_to_delete = st.selectbox(
                        "Selecione o utilizador a eliminar:",
                        [f"{u['id']} - {u['username']}" for u in utilizadores]
                    )
                    
                    if user_to_delete:
                        user_id = int(user_to_delete.split(" - ")[0])
                        selected_user = next(u for u in utilizadores if u['id'] == user_id)
                        
                        # Evitar eliminar o próprio administrador
                        if selected_user['username'] == st.session_state["username"]:
                            st.error("Não podes eliminar o teu próprio utilizador!")
                        else:
                            confirm = st.checkbox(f"Confirmar eliminação de {selected_user['username']}?")
                            if confirm and st.button("Eliminar Utilizador"):
                                eliminar_utilizador(user_id)
                            st.rerun()
                else:
                    st.info("Não existem utilizadores registados.")
        else:
            # Utilizador regular
            st.write("Acesso de Utilizador Regular")
            st.write("Aqui poderás gerir as tuas informações pessoais e wishlist")
            
            if st.button("Logout", key="btn_logout_regular"):
                logout()
                st.rerun()
    else:
        # Tabs para login e registro
        tab1, tab2 = st.tabs(["Login", "Registro"])
        
        with tab1:
            with st.form("login_form"):
                username = st.text_input("Nome de Utilizador")
                password_hash = st.text_input("Password", type="password")
                submit = st.form_submit_button("Iniciar Sessão")
                
                if submit:
                    if username and password_hash:
                        if check_login(username, password_hash):
                            st.rerun()
                    else:
                        st.error("Por favor, preencha todos os campos.")
        
        with tab2:
            with st.form("registro_form"):
                new_username = st.text_input("Nome de Utilizador")
                new_password_hash = st.text_input("Password", type="password")
                confirm_password_hash = st.text_input("Confirmar Password", type="password")
                nome = st.text_input("Nome Completo")
                email = st.text_input("Email")
                submit_registro = st.form_submit_button("Registar")
                
                if submit_registro:
                    if new_username and new_password_hash and confirm_password_hash and nome and email:
                        if new_password_hash != confirm_password_hash:
                            st.error("As password_hashs não coincidem!")
                        elif len(new_password_hash) < 3:
                            st.error("A password_hash deve ter pelo menos 3 caracteres.")
                        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                            st.error("Email inválido.")
                        else:
                            if regista_utilizador(new_username, new_password_hash, nome, email):
                                st.info("Registo concluído! Faz login para continuar.")
                    else:
                        st.error("Por favor, preencha todos os campos.")

# ------------------------------------------------
# 6. SEÇÕES EXTRA (PLACEHOLDERS)
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
# 7. MAIN (EXECUÇÃO PRINCIPAL DO STREAMLIT)
# ------------------------------------------------

def main():
    # Criar base de dados e tabela, se não existirem
    cria_tabelas()
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
    /* Status de utilizador */
    .user-status {
        padding: 5px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 10px;
    }
    .logged-in {
        background-color: #d4edda;
        color: #155724;
    }
    .logged-out {
        background-color: #f8d7da;
        color: #721c24;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Título e barra de topo
    st.title("Gestão de Produtos - Loja de Moda")
    st.markdown('<div class="title-bar">Loja de Moda</div>', unsafe_allow_html=True)
    
    # Barra de topo (pesquisa e links rápidos)
    col1, col2, col3 = st.columns([3, 4, 1])
    with col1:
        st.session_state["search"] = st.text_input("Pesquisar", value=st.session_state["search"], placeholder="Pesquisar produtos...")
    with col2:
        st.markdown("""
        **[Descontos](#) | [Mais Vendidos](#) | [Marcas](#) | [Suporte](#) | [Entregas](#)**
        """)
    with col3:
        if st.button("Wishlist"):
            st.session_state["current_page"] = "Wishlist"
    
    # Mostrar status do utilizador
    if st.session_state["logged_in"]:
        st.sidebar.markdown(f'<div class="user-status logged-in">Olá, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<div class="user-status logged-out">Não autenticado</div>', unsafe_allow_html=True)
    
    # # Menu lateral usando streamlit-option_menu
    with st.sidebar:
        if st.session_state["is_admin"] == True: 
          escolha = option_menu(
              "Menu",
              ["Home", "Produtos", "Adicionar", "Editar", "Eliminar", "Wishlist", "Conta"],
              icons=["house", "cart", "plus", "pencil", "trash", "heart", "person"],
              menu_icon="list",
              default_index=0
            )
        else:
            if st.session_state["logged_in"] == True: 
                escolha = option_menu(
                "Menu",
                ["Home", "Produtos", "Wishlist", "Conta"],
                icons=["house", "cart", "heart", "person"],
                menu_icon="list",
                default_index=0
            )
            else:
                escolha = option_menu(
                "Menu",
                ["Home", "Produtos", "Conta"],
                icons=["house", "cart", "person"],
                menu_icon="list",
                default_index=0
                )
    
    
    # Atualizar a página atual
    st.session_state["current_page"] = escolha
    
    # Lógica de navegação
    if escolha == "Home":
        home_page()
    elif escolha == "Produtos":
        produtos_page()
    elif escolha == "Adicionar":
        adicionar_page()
    elif escolha == "Editar":
        editar_page() 
    elif escolha == "Eliminar":
        eliminar_page()
    elif escolha == "Wishlist":
        wishlist_page()
    elif escolha == "Conta":
        login_page()

if __name__ == "__main__":
    main()