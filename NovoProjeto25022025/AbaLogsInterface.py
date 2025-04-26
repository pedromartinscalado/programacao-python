import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Função para obter a conexão MySQL
def obter_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loja_roupa_bd"
    )


# Função para obter as tabelas existentes
def obter_tabelas():
    try:
        mydb = obter_conexao()
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        cursor.close()
        mydb.close()
        return [t[0] for t in tabelas]
    except mysql.connector.Error as erro:
        log_erro(f"Erro ao obter tabelas: {erro}")
        return []


# Função para verificar se o nome da tabela é válido e não existe
def tabela_existe(nome_tabela):
    try:
        mydb = obter_conexao()
        cursor = mydb.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{nome_tabela}'")
        resultado = cursor.fetchone()
        cursor.close()
        mydb.close()
        return resultado is not None
    except mysql.connector.Error as erro:
        log_erro(f"Erro ao verificar a tabela: {erro}")
        return False


# Função para apagar uma tabela selecionada
def apagar_tabela():
    nome_tabela = listbox_tabelas.get(tk.ACTIVE)
    if not nome_tabela:
        messagebox.showwarning("Atenção", "Selecione uma tabela para apagar.")
        return

    resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja apagar a tabela '{nome_tabela}'?")
    if resposta:
        try:
            mydb = obter_conexao()
            cursor = mydb.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
            mydb.commit()
            cursor.close()
            mydb.close()
            messagebox.showinfo("Sucesso", f"Tabela '{nome_tabela}' apagada com sucesso!")
            atualizar_lista_tabelas()
        except mysql.connector.Error as erro:
            log_erro(f"Erro ao apagar a tabela: {erro}")


# Função para renomear uma tabela
def renomear_tabela():
    nome_tabela = listbox_tabelas.get(tk.ACTIVE)
    novo_nome = entry_novo_nome.get().strip()
    if not nome_tabela or not novo_nome.isidentifier():
        messagebox.showerror("Erro", "Nome inválido. Selecione uma tabela e insira um novo nome válido.")
        return

    if tabela_existe(novo_nome):
        messagebox.showerror("Erro", f"A tabela '{novo_nome}' já existe!")
        return

    try:
        mydb = obter_conexao()
        cursor = mydb.cursor()
        cursor.execute(f"RENAME TABLE {nome_tabela} TO {novo_nome}")
        mydb.commit()
        cursor.close()
        mydb.close()
        messagebox.showinfo("Sucesso", f"Tabela '{nome_tabela}' renomeada para '{novo_nome}' com sucesso!")
        atualizar_lista_tabelas()
    except mysql.connector.Error as erro:
        log_erro(f"Erro ao renomear a tabela: {erro}")


# Função para criar uma nova tabela
def criar_tabela():
    nome_tabela = entry_nome_tabela.get().strip()
    if not nome_tabela.isidentifier():
        messagebox.showerror("Erro", "Nome da tabela inválido! Use apenas letras e sublinhados.")
        return

    if tabela_existe(nome_tabela):
        messagebox.showerror("Erro", f"A tabela '{nome_tabela}' já existe!")
        return

    try:
        mydb = obter_conexao()
        cursor = mydb.cursor()
        query = f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            descricao TEXT
        )"""
        cursor.execute(query)
        mydb.commit()
        cursor.close()
        mydb.close()
        messagebox.showinfo("Sucesso", f"Tabela '{nome_tabela}' criada com sucesso!")
        atualizar_lista_tabelas()
    except mysql.connector.Error as erro:
        log_erro(f"Erro ao criar a tabela: {erro}")


# Função para atualizar a lista de tabelas
def atualizar_lista_tabelas():
    listbox_tabelas.delete(0, tk.END)
    for tabela in obter_tabelas():
        listbox_tabelas.insert(tk.END, tabela)


# Função para registrar logs de erro
def log_erro(mensagem):
    logs.insert(tk.END, f"ERRO: {mensagem}")
    logs.yview(tk.END)  # rolar para o final
    print(mensagem)  # Imprimir no terminal também, se necessário


# Criar interface gráfica
root = tk.Tk()
root.title("Gerenciador de Tabelas - MySQL")
root.geometry("500x550")

# Criar uma aba de logs
notebook = ttk.Notebook(root)
aba_principal = tk.Frame(notebook)
aba_logs = tk.Frame(notebook)

notebook.add(aba_principal, text="Principal")
notebook.add(aba_logs, text="Logs")
notebook.pack(expand=True, fill="both")

# --- Aba Principal ---
# Entrada para criar nova tabela
tk.Label(aba_principal, text="Nome da Nova Tabela:").pack()
entry_nome_tabela = tk.Entry(aba_principal, width=30)
entry_nome_tabela.pack(pady=5)
btn_criar = tk.Button(aba_principal, text="Criar Tabela", command=criar_tabela)
btn_criar.pack(pady=5)

# Lista de tabelas existentes
tk.Label(aba_principal, text="Tabelas Existentes:").pack()
listbox_tabelas = tk.Listbox(aba_principal, height=10, width=40)
listbox_tabelas.pack(pady=5)

btn_apagar = tk.Button(aba_principal, text="Apagar Tabela", command=apagar_tabela)
btn_apagar.pack(pady=5)

# Entrada e botão para renomear tabela
tk.Label(aba_principal, text="Novo Nome da Tabela:").pack()
entry_novo_nome = tk.Entry(aba_principal, width=30)
entry_novo_nome.pack(pady=5)
btn_renomear = tk.Button(aba_principal, text="Renomear Tabela", command=renomear_tabela)
btn_renomear.pack(pady=5)

btn_atualizar = tk.Button(aba_principal, text="Atualizar Lista", command=atualizar_lista_tabelas)
btn_atualizar.pack(pady=5)

# --- Aba de Logs ---
logs_label = tk.Label(aba_logs, text="Logs de Erros:", font=("Arial", 14))
logs_label.pack(pady=10)
logs = tk.Listbox(aba_logs, height=15, width=60)
logs.pack(padx=10, pady=10)

# Inicializa a interface
atualizar_lista_tabelas()
root.mainloop()
