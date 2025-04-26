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
        hashed_password_hash = bcrypt.hashpw(password_hash.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO utilizadores (username, password_hash, nome, email, is_admin) VALUES (%s, %s, %s, %s, %s)",
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
    """Verifica as credenciais na base de dados usando bcrypt e retorna dados do utilizador.""" # Alterado comentário
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM utilizadores WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user:
            if bcrypt.checkpw(password_hash.encode('utf-8'), user['password_hash'].encode('utf-8')):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["user_id"] = user["id"]
                st.session_state["is_admin"] = user["is_admin"]
                st.session_state["user_nome"] = user["nome"] # *** NOVO: Guardar nome na sessão ***
                st.session_state["user_email"] = user["email"] # *** NOVO: Guardar email na sessão ***
                st.success(f"Bem-vindo, {username}!")
                return True
            else:
                st.error("password inválida. Tente novamente.")
                return False
        else:
            st.error("Utilizador não encontrado. Verifique o nome de utilizador.") # Corrected typo and indentation
            return False # Added return False in else block for consistency
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
    st.session_state["user_nome"] = None # *** NOVO: Limpar nome da sessão no logout ***
    st.session_state["user_email"] = None # *** NOVO: Limpar email da sessão no logout ***
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

def atualizar_utilizador(id_utilizador, nome, email): # *** FUNÇÃO ADICIONADA ***
    """Atualiza o nome e email de um utilizador na base de dados."""
    conn = get_db_connection()
    if conn is None:
        return False # Indica falha na ligação

    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE utilizadores SET nome = %s, email = %s WHERE id = %s",
            (nome, email, id_utilizador)
        )
        conn.commit()
        return True # Indica sucesso na atualização
    except mysql.connector.Error as err:
        st.error(f"Erro ao atualizar utilizador: {err}")
        return False # Indica falha na atualização
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
    if "wishlist_clicked" not in st.session_state:
        st.session_state["wishlist_clicked"] = False
    if "user_nome" not in st.session_state: # *** NOVO: Inicializar user_nome na sessão ***
        st.session_state["user_nome"] = None
    if "user_email" not in st.session_state: # *** NOVO: Inicializar user_email na sessão ***
        st.session_state["user_email"] = None


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
    MAX_NOME_LENGTH = 100
    MAX_DESCRICAO_LENGTH = 500
    MAX_IMAGE_SIZE_BYTES = 2 * 1024 * 1024 # 2MB

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
            elif len(nome) > MAX_NOME_LENGTH:
                st.error(f'O nome do produto não pode ter mais de {MAX_NOME_LENGTH} caracteres.')
            elif nome.isdigit():
                st.error('O nome do produto não pode conter apenas números.')
            elif not re.match(pattern, nome):
                st.error('O nome do produto contém caracteres inválidos.')
            elif descricao.strip() == "":
                st.error('A descrição não pode estar vazia.')
            elif len(descricao) > MAX_DESCRICAO_LENGTH:
                st.error(f'A descrição do produto não pode ter mais de {MAX_DESCRICAO_LENGTH} caracteres.')
            elif not re.match(pattern, descricao):
                st.error('A descrição contém caracteres inválidos.')
            elif preco <= 0:
                st.error('O preço deve ser maior que zero.')
            else:
                # Processar e sanitizar a imagem
                if imagem_file is not None:
                    if imagem_file.size > MAX_IMAGE_SIZE_BYTES:
                        st.error(f"A imagem é demasiado grande. O tamanho máximo permitido é {MAX_IMAGE_SIZE_BYTES/(1024*1024):.2f} MB.")
                        imagem_path = None # Para não tentar processar uma imagem inválida
                    else:
                        imagem_nome = sanitize_filename(imagem_file.name)
                        imagem_path = os.path.join("images", imagem_nome)
                        with open(imagem_path, "wb") as f:
                            f.write(imagem_file.getbuffer())
                else:
                    imagem_path = NO_IMAGE_PATH
                if imagem_path: # Só adicionar o produto se não houve erro na imagem (ou se não foi carregada imagem, usando NO_IMAGE_PATH)
                    adiciona_produto(nome, descricao, preco, imagem_path)

def editar_page():
    st.subheader("Editar Produto")
    MAX_NOME_LENGTH = 100
    MAX_DESCRICAO_LENGTH = 500
    MAX_IMAGE_SIZE_BYTES = 2 * 1024 * 1024 # 2MB

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
                elif len(nome) > MAX_NOME_LENGTH:
                    st.error(f'O nome do produto não pode ter mais de {MAX_NOME_LENGTH} caracteres.')
                elif nome.isdigit():
                    st.error('O nome do produto não pode conter apenas números.')
                elif not re.match(pattern, nome):
                    st.error('O nome contém caracteres inválidos.')
                elif descricao.strip() == "":
                    st.error('A descrição não pode estar vazia.')
                elif len(descricao) > MAX_DESCRICAO_LENGTH:
                    st.error(f'A descrição do produto não pode ter mais de {MAX_DESCRICAO_LENGTH} caracteres.')
                elif not re.match(pattern, descricao):
                    st.error('A descrição contém caracteres inválidos.')
                elif preco <= 0:
                    st.error('O preço deve ser maior que zero.')
                else:
                    if imagem_file is not None:
                        if imagem_file.size > MAX_IMAGE_SIZE_BYTES:
                            st.error(f"A imagem é demasiado grande. O tamanho máximo permitido é {MAX_IMAGE_SIZE_BYTES/(1024*1024):.2f} MB.")
                            imagem_path = None # Para não tentar processar uma imagem inválida
                        else:
                            imagem_nome = sanitize_filename(imagem_file.name)
                            imagem_path = os.path.join("images", imagem_nome)
                            with open(imagem_path, "wb") as f:
                                f.write(imagem_file.getbuffer())
                    else:
                        imagem_path = produto['imagem']
                    if imagem_path: # Só atualizar o produto se não houve erro na imagem (ou se não foi carregada imagem)
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
        with st.container(): # *** NOVO: Container para a área de perfil ***
            st.subheader("Perfil de Utilizador") # Título da secção de perfil
            st.write(f"Bem-vindo, **{st.session_state['username']}**!") # Mensagem de boas-vindas (mantém-se ou ajusta-se)

            # *** CAMPOS EDITÁVEIS PARA NOME E EMAIL (MANTÉM-SE) ***
            nome_perfil = st.text_input("Nome Completo", value=st.session_state['user_nome'] if st.session_state['user_nome'] else "")
            email_perfil = st.text_input("Email", value=st.session_state['user_email'] if st.session_state['user_email'] else "")

            st.write("---") # Separador visual

            st.subheader("Alterar Password") # Subtítulo para a secção de alterar password

            # *** NOVOS CAMPOS PARA ALTERAR PASSWORD ***
            password_atual_perfil = st.text_input("Password Atual", type="password") # Campo para password atual
            nova_password_perfil = st.text_input("Nova Password", type="password") # Campo para nova password
            confirmar_nova_password_perfil = st.text_input("Confirmar Nova Password", type="password") # Campo para confirmar nova password

        if st.button("Salvar Perfil", key="btn_salvar_perfil"):
            # *** Lógica para VALIDAR e GUARDAR NOME e EMAIL (apenas perfil) ***
            user_id = st.session_state["user_id"]
            nome = nome_perfil
            email = email_perfil

            if not nome.strip():
                st.error("Por favor, insira o seu Nome Completo.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Email inválido. Por favor, insira um email no formato correto (ex: exemplo@dominio.com).")
            else:  # *** THIS ELSE BLOCK MUST BE INDENTED INSIDE the 'if st.button' ***
                if atualizar_utilizador(user_id, nome, email): # *** THIS IF AND EVERYTHING BELOW MUST BE FURTHER INDENTED ***
                    st.success("Perfil atualizado com sucesso!")
                    st.session_state['user_nome'] = nome
                    st.session_state['user_email'] = email
                else:
                    st.error("Erro ao atualizar o perfil. Tente novamente.")
                    
            if not nome.strip():
                st.error("Por favor, insira o seu Nome Completo.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Email inválido. Por favor, insira um email no formato correto (ex: exemplo@dominio.com).")
            else:
                if atualizar_utilizador(user_id, nome, email):
                    st.success("Perfil atualizado com sucesso!")
                    st.session_state['user_nome'] = nome
                    st.session_state['user_email'] = email
                else:
                    st.error("Erro ao atualizar o perfil. Tente novamente.")
                    
            
            
        if st.button("Alterar Password", key="btn_alterar_password"):
            # *** Lógica para VALIDAR PASSWORD ATUAL, NOVA PASSWORD e ALTERAR PASSWORD ***
            password_atual = password_atual_perfil
            nova_password = nova_password_perfil
            confirmar_nova_password = confirmar_nova_password_perfil
            user_id = st.session_state["user_id"]

            if not password_atual: # *** INDENTADO CORRETAMENTE: DENTRO do 'if st.button' block ***
                st.error("Por favor, insira a sua Password Atual para alterar a password.")
            elif not nova_password or not confirmar_nova_password:
                st.error("Por favor, preencha os campos 'Nova Password' e 'Confirmar Nova Password'.")
            elif nova_password != confirmar_nova_password:
                st.error("As novas passwords não coincidem.")
            else:
                # *** VERIFICAR PASSWORD ATUAL E (FUTURAMENTE) ALTERAR PASSWORD ***
                conn = get_db_connection()
                if conn:
                    cursor = conn.cursor(dictionary=True)
                    cursor.execute("SELECT password_hash FROM utilizadores WHERE id = %s", (user_id,))
                    user_data = cursor.fetchone()
                    cursor.close()
                    conn.close()

                    if user_data:
                        stored_password_hash = user_data['password_hash']
                        if bcrypt.checkpw(password_atual.encode('utf-8'), stored_password_hash.encode('utf-8')):
                            st.success("Password Atual verificada com sucesso! (Alteração de password ainda não implementada)")  # Mensagem de teste
                        else:
                            st.error("Password Atual incorreta. Por favor, tente novamente.")
                    else:
                        st.error("Erro ao verificar password atual. Tente novamente.")
                else:
                    st.error("Erro ao conectar à base de dados.")   
            

        if st.session_state["is_admin"]:
            st.success("Acesso de Administrador")

            # Tabs para diferentes funções de administrador
            tab1, tab2 = st.tabs(["Perfil", "Gestão de Utilizadores"])

            with tab1:
                st.subheader("Informações do Perfil")
                st.write("Aqui poderás alterar as tuas informações pessoais (funcionalidade em desenvolvimento)")
                # *** O BOTÃO "Logout" NÃO DEVE ESTAR AQUI DENTRO DO tab1! ***

            with tab2:
                st.subheader("Gerir Utilizadores")
                utilizadores = lista_utilizadores()
                # *** O BOTÃO "Logout" NÃO DEVE ESTAR AQUI DENTRO DO tab2! ***

            if st.button("Logout", key="btn_logout_admin"): # *** BOTÃO "Logout" FORA DOS TABS! INDENTADO CORRETAMENTE! ***
                logout()
                st.rerun()
                
                # Utilizador regular
            else:
                    st.info("Acesso de Utilizador Regular")
                    st.write("Aqui poderá ver e editar as suas informações de perfil.") # Mensagem descritiva ajustada

                    if st.button("Logout", key="btn_logout_regular"):
                        logout()
                        st.rerun()
    else:
        # Tabs para login e registo
        tab1, tab2 = st.tabs(["Login", "Registo"])

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
            with st.form("registo_form"):
                new_username = st.text_input("Nome de Utilizador")
                new_password_hash = st.text_input("Password", type="password")
                confirm_password_hash = st.text_input("Confirmar Password", type="password")
                nome = st.text_input("Nome Completo")
                email = st.text_input("Email")
                submit_registo = st.form_submit_button("Registar")

                if submit_registo:
                    if new_username and new_password_hash and confirm_password_hash and nome and email:
                        if new_password_hash != confirm_password_hash:
                            st.error("As password não coincidem!")
                        elif len(new_password_hash) < 3:
                            st.error("A password deve ter pelo menos 3 caracteres.")
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
            st.rerun()

    # Mostrar status do utilizador
    if st.session_state["logged_in"]:
        st.sidebar.markdown(f'<div class="user-status logged-in">Olá, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<div class="user-status logged-out">Não autenticado</div>', unsafe_allow_html=True)

    menu_options = ["Home", "Produtos", "Conta"]
    menu_icons = ["house", "cart", "person"]

    if st.session_state["logged_in"]:
        menu_options = ["Home", "Produtos", "Wishlist", "Conta"]
        menu_icons = ["house", "cart", "heart", "person"]

    if st.session_state["is_admin"]:
        menu_options = ["Home", "Produtos", "Adicionar", "Editar", "Eliminar", "Wishlist", "Conta"]
        menu_icons = ["house", "cart", "plus", "pencil", "trash", "heart", "person"]

    default_index = menu_options.index(st.session_state["current_page"]) if st.session_state["current_page"] in menu_options else 0
    with st.sidebar:
        escolha = option_menu(
            "Menu",
            menu_options,
            icons=menu_icons,
            menu_icon="list",
            default_index=menu_options.index(st.session_state["current_page"])
        )

        if not st.session_state["wishlist_clicked"] or escolha != "Wishlist":
            st.session_state["current_page"] = escolha

    # Lógica de navegação
    if st.session_state["current_page"] == "Home":
        home_page()
    elif st.session_state["current_page"] == "Produtos":
        produtos_page()
    elif st.session_state["current_page"] == "Adicionar":
        adicionar_page()
    elif st.session_state["current_page"] == "Editar":
        editar_page()
    elif st.session_state["current_page"] == "Eliminar":
        eliminar_page()
    elif st.session_state["current_page"] == "Wishlist":
        wishlist_page()
    elif st.session_state["current_page"] == "Conta":
        login_page()

if __name__ == "__main__":
    main()