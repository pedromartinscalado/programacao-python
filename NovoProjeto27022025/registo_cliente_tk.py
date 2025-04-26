import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re 
##Crie uma aplicação usando a classe Tkinter
##que permita inserir dados na tabela clientes. 
##Inclua:
##Título
##Descrição breve
##Campos para introdução de Nome, Telefone, Email, e Localidade;
##Um botão "Guardar" que execute a inserção dos dados na base de dados. 

class AppInserirClienteMySQL:
    def __init__(self, master):
        self.master = master
        master.title("Inserir Clientes na Base de Dados")

        # Título da Aplicação
        self.titulo = tk.Label(master, text="Registar Novo Cliente", font=('Arial', 16, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Descrição
        self.descricao = tk.Label(master, text="Por favor, preencha os detalhes do cliente abaixo.", font=('Arial', 10))
        self.descricao.grid(row=1, column=0, columnspan=2, pady=5)

        # Campos de Entrada
        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        self.nome_entry = tk.Entry(master)
        self.nome_entry.grid(row=2, column=1, padx=5, pady=5)

        self.telefone_label = tk.Label(master, text="Telefone:")
        self.telefone_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
        self.telefone_entry = tk.Entry(master)
        self.telefone_entry.grid(row=3, column=1, padx=5, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        self.localidade_label = tk.Label(master, text="Localidade:")
        self.localidade_label.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)
        self.localidade_entry = tk.Entry(master)
        self.localidade_entry.grid(row=5, column=1, padx=5, pady=5)

        # Botão Guardar
        self.guardar_button = ttk.Button(master, text="Guardar", command=self.guardar_dados)
        self.guardar_button.grid(row=6, column=0, columnspan=2, pady=20)

    def validar_nome(self, nome):
        return nome.replace(" ", "").isalpha()

    def validar_telefone(self, telefone):
        return telefone.isdigit()

    def validar_email(self, email):
        email_regex = r'^[\w.-]+@[\w.-]+\.\w+$'
        return re.fullmatch(email_regex, email)

    def conectar_bd(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS clientesdb")
            cursor.close()
            mydb.close()

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="clientesdb"
            )
            return mydb
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
            return None

    def guardar_dados(self):
        nome = self.nome_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
        email = self.email_entry.get().strip()
        localidade = self.localidade_entry.get().strip()

        if not nome or not telefone or not email or not localidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        if not self.validar_nome(nome):
            messagebox.showerror("Erro", "Nome inválido. Por favor, use apenas letras e espaços.")
            return

        if not self.validar_telefone(telefone):
            messagebox.showerror("Erro", "Telefone inválido. Por favor, use apenas números.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "Email inválido. Por favor, insira um email no formato correto.")
            return

        mydb = self.conectar_bd()
        if not mydb:
            return

        try:
            cursor = mydb.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    telefone VARCHAR(20) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    localidade VARCHAR(255) NOT NULL
                )
            """)
            sql = "INSERT INTO clientes (nome, telefone, email, localidade) VALUES (%s, %s, %s, %s)"
            val = (nome, telefone, email, localidade)
            cursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Sucesso", "O Cliente foi registado com sucesso!")

            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.localidade_entry.delete(0, tk.END)
        
        except mysql.connector.Error as e:
            messagebox.showerror("Erro ao guardar os dados", f"Ocorreu um erro ao guardar os dados: {e}")
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppInserirClienteMySQL(root)
    root.mainloop()
