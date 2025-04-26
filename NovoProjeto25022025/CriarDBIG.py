import tkinter as tk
import mysql.connector
from tkinter import messagebox
import re  # Para validar o nome da base de dados usando expressões regulares

# Função para validar o nome da base de dados
def validar_nome_base(nome_base):
    # Verificar se o nome está vazio
    if not nome_base:
        return False, "O nome da base de dados não pode estar vazio."
    
    # Verificar se o nome contém espaços em branco ou caracteres especiais
    # Expressão regular que só permite letras, números e underscores (sem espaços no início ou fim)
    if not re.match("^[A-Za-z0-9_]+$", nome_base):
        return False, "O nome da base de dados deve conter apenas letras, números e underscores (sem espaços)."
    
    # Verificar se o nome é apenas número (agora verificando se contém pelo menos uma letra)
    if nome_base.isdigit() or nome_base.isnumeric():
        return False, "O nome da base de dados não pode ser apenas um número."
    
    # Verificar se o nome contém pelo menos uma letra
    if not any(c.isalpha() for c in nome_base):
        return False, "O nome da base de dados deve conter pelo menos uma letra."
    
    return True, ""

# Função para criar uma nova base de dados
def criar_base():
    nome_base = entry_nome_base.get()  # Obter o nome da base de dados do campo de entrada
    
    # Validar o nome da base de dados
    valido, mensagem = validar_nome_base(nome_base)
    if not valido:
        messagebox.showwarning("Atenção", mensagem)
        return
    
    try:
        # Conexão com o MySQL
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',  
            password=''  # Coloque a senha se necessário
        )
        
        cursor_inicial = conexao_inicial.cursor()
        
        # Criar a base de dados (usando crase para garantir que o nome seja tratado corretamente, mesmo que seja numérico)
        cursor_inicial.execute(f"CREATE DATABASE IF NOT EXISTS `{nome_base}`")  # Usando crase para escapar o nome
        conexao_inicial.close()
        
        # Exibir uma mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Base de dados '{nome_base}' criada com sucesso!")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao criar a base de dados: {err}")

# Função para renomear a base de dados
def renomear_base():
    nome_base_atual = entry_nome_base_atual.get()  # Obter o nome da base de dados atual
    novo_nome_base = entry_novo_nome_base.get()  # Obter o novo nome da base de dados
    
    # Validar os nomes da base de dados
    valido, mensagem = validar_nome_base(novo_nome_base)
    if not valido:
        messagebox.showwarning("Atenção", mensagem)
        return
    
    try:
        # Conexão com o MySQL
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',  
            password=''  # Coloque a senha se necessário
        )
        
        cursor_inicial = conexao_inicial.cursor()
        
        # Renomear a base de dados
        cursor_inicial.execute(f"RENAME DATABASE `{nome_base_atual}` TO `{novo_nome_base}`")  # Usando crase para escapar o nome
        conexao_inicial.close()
        
        # Exibir uma mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Base de dados '{nome_base_atual}' renomeada para '{novo_nome_base}' com sucesso!")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao renomear a base de dados: {err}")

# Criar a janela principal
root = tk.Tk()
root.title("Gerenciar Base de Dados")

# Configurar o tamanho da janela
root.geometry("400x400")

# Criar uma Label
label_instrucoes = tk.Label(root, text="Digite o nome da base de dados para criar ou renomear:")
label_instrucoes.pack(pady=10)

# Criar o campo de entrada para o nome da base de dados atual
label_nome_base_atual = tk.Label(root, text="Nome da Base de Dados Atual (se renomeando):")
label_nome_base_atual.pack(pady=5)

entry_nome_base_atual = tk.Entry(root, width=30)
entry_nome_base_atual.pack(pady=5)

# Criar o campo de entrada para o novo nome da base de dados
label_novo_nome_base = tk.Label(root, text="Novo Nome da Base de Dados:")
label_novo_nome_base.pack(pady=5)

entry_novo_nome_base = tk.Entry(root, width=30)
entry_novo_nome_base.pack(pady=5)

# Criar o campo de entrada para o nome da base de dados (para criar)
label_nome_base = tk.Label(root, text="Nome da Base de Dados (para criar):")
label_nome_base.pack(pady=5)

entry_nome_base = tk.Entry(root, width=30)
entry_nome_base.pack(pady=5)

# Criar o botão para criar a base de dados
btn_criar = tk.Button(root, text="Criar Base de Dados", command=criar_base, width=20)
btn_criar.pack(pady=10)

# Criar o botão para renomear a base de dados
btn_renomear = tk.Button(root, text="Renomear Base de Dados", command=renomear_base, width=20)
btn_renomear.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()


