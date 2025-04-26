import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Função para obter as tabelas existentes
def obter_tabelas():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_roupa_bd"
        )
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        cursor.close()
        mydb.close()
        return [t[0] for t in tabelas]
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao obter tabelas: {erro}")
        return []

# Função para apagar uma tabela selecionada
def apagar_tabela():
    nome_tabela = listbox_tabelas.get(tk.ACTIVE)
    if not nome_tabela:
        messagebox.showwarning("Atenção", "Selecione uma tabela para apagar.")
        return

    resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja apagar a tabela '{nome_tabela}'?")
    if resposta:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="loja_roupa_bd"
            )
            cursor = mydb.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
            mydb.commit()
            cursor.close()
            mydb.close()
            messagebox.showinfo("Sucesso", f"Tabela '{nome_tabela}' apagada com sucesso!")
            atualizar_lista_tabelas()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro", f"Erro ao apagar a tabela: {erro}")

# Função para renomear uma tabela
def renomear_tabela():
    nome_tabela = listbox_tabelas.get(tk.ACTIVE)
    novo_nome = entry_novo_nome.get().strip()
    if not nome_tabela or not novo_nome.isidentifier():
        messagebox.showerror("Erro", "Nome inválido. Selecione uma tabela e insira um novo nome válido.")
        return

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_roupa_bd"
        )
        cursor = mydb.cursor()
        cursor.execute(f"RENAME TABLE {nome_tabela} TO {novo_nome}")
        mydb.commit()
        cursor.close()
        mydb.close()
        messagebox.showinfo("Sucesso", f"Tabela '{nome_tabela}' renomeada para '{novo_nome}' com sucesso!")
        atualizar_lista_tabelas()
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao renomear a tabela: {erro}")

# Função para criar uma nova tabela
def criar_tabela():
    nome_tabela = entry_nome_tabela.get().strip()
    if not nome_tabela.isidentifier():
        messagebox.showerror("Erro", "Nome da tabela inválido! Use apenas letras e sublinhados.")
        return

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_roupa_bd"
        )
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
        messagebox.showerror("Erro", f"Erro ao criar a tabela: {erro}")

# Função para atualizar a lista de tabelas
def atualizar_lista_tabelas():
    listbox_tabelas.delete(0, tk.END)
    for tabela in obter_tabelas():
        listbox_tabelas.insert(tk.END, tabela)

# Criar interface gráfica
root = tk.Tk()
root.title("Gerenciador de Tabelas - MySQL")
root.geometry("400x550")

# Entrada para criar nova tabela
tk.Label(root, text="Nome da Nova Tabela:").pack()
entry_nome_tabela = tk.Entry(root, width=30)
entry_nome_tabela.pack(pady=5)
btn_criar = tk.Button(root, text="Criar Tabela", command=criar_tabela)
btn_criar.pack(pady=5)

# Lista de tabelas existentes
tk.Label(root, text="Tabelas Existentes:").pack()
listbox_tabelas = tk.Listbox(root, height=10, width=40)
listbox_tabelas.pack(pady=5)

btn_apagar = tk.Button(root, text="Apagar Tabela", command=apagar_tabela)
btn_apagar.pack(pady=5)

# Entrada e botão para renomear tabela
tk.Label(root, text="Novo Nome da Tabela:").pack()
entry_novo_nome = tk.Entry(root, width=30)
entry_novo_nome.pack(pady=5)
btn_renomear = tk.Button(root, text="Renomear Tabela", command=renomear_tabela)
btn_renomear.pack(pady=5)

btn_atualizar = tk.Button(root, text="Atualizar Lista", command=atualizar_lista_tabelas)
btn_atualizar.pack(pady=5)

atualizar_lista_tabelas()
root.mainloop()
