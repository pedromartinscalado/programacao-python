#pip install streamlit mysql-connector-python
#streamlit run target nome da app (neste exemplo:19_InserirProdutosStreamlit.py)
 
 
import streamlit as st
import mysql.connector
from mysql.connector import Error
 
# Função para inserir dados na base de dados
def inserir_produto(produto_nome, produto_descrit, produto_preco, produto_quantidade):
    try:
        # Ligar à base de dados
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtestestabelas"
        )
        # Verificar se a conexão foi bem-sucedida
        if mydb.is_connected():
            st.success("Conexão com a base de dados realizada com sucesso!")
        mycursor = mydb.cursor()
 
        # Inserir dados na tabela Produtos
        sql = """
        INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade) 
        VALUES (%s, %s, %s, %s)
        """
        val = (produto_nome, produto_descrit, produto_preco, produto_quantidade)
        mycursor.execute(sql, val)
        # Confirmar a inserção dos dados
        mydb.commit()
        st.success("Produto inserido com sucesso!")
 
    except Error as err:
        st.error(f"Erro ao inserir o produto: {err}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
 
# Configuração da página
st.set_page_config(page_title="Inserir Produto", layout="centered")
 
# Título da aplicação
st.title("Gestão de Produtos")
 
# Formulário para inserir os dados do produto
st.subheader("Inserir um novo produto")
 
# Entradas do utilizador
produto_nome = st.text_input("Nome do Produto")
produto_descrit = st.text_area("Descrição do Produto")
produto_preco = st.number_input("Preço do Produto", min_value=0.0, step=0.01)
produto_quantidade = st.number_input("Quantidade do Produto", min_value=0, step=1)
 
# Botão para submeter
if st.button("Inserir Produto"):
    if produto_nome and produto_descrit and produto_preco > 0 and produto_quantidade > 0:
        inserir_produto(produto_nome, produto_descrit, produto_preco, produto_quantidade)
    else:
        st.warning("Preencha todos os campos corretamente antes de submeter!")
 
# Instrução adicional
st.info("Preencha os campos acima e clique no botão para inserir os dados na base de dados.")
