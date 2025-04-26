import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Função para criar a base de dados
def criar_banco():
    try:
        # Conexão inicial para criar a base de dados
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  
        )
        
        cursor_inicial = conexao_inicial.cursor()
        cursor_inicial.execute("CREATE DATABASE IF NOT EXISTS Banco")
        cursor_inicial.close()
        conexao_inicial.close()

        messagebox.showinfo("Sucesso", "Base de dados criada com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao criar a base de dados: {err}")

# Função para apagar a base de dados
def apagar_banco():
    try:
        # Conexão inicial para apagar a base de dados
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',  
            password=''  
        )
        
        cursor_inicial = conexao_inicial.cursor()
        cursor_inicial.execute("DROP DATABASE IF EXISTS Banco")
        cursor_inicial.close()
        conexao_inicial.close()

        messagebox.showinfo("Sucesso", "Base de dados apagada com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao apagar a base de dados: {err}")

# Criar a janela principal
root = tk.Tk()
root.title("Gestão de Base de Dados")

# Configurar o tamanho da janela
root.geometry("300x200")

# Criar os botões
btn_criar = tk.Button(root, text="Criar Base de Dados", command=criar_banco, width=20)
btn_criar.pack(pady=20)

btn_apagar = tk.Button(root, text="Apagar Base de Dados", command=apagar_banco, width=20)
btn_apagar.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
