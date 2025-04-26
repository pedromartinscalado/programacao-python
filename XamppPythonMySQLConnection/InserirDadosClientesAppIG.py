import tkinter as tk  # Importa o módulo tkinter
from tkinter import messagebox  # Para apresentar mensagens
import mysql.connector  # Para interagir com MySQL
import re  # Biblioteca para validação de email e telefone


# Função para validar e inserir dados na tabela Clientes
def inserir_dados():
    # Recolher os dados do formulário
    nome = entry_nome.get().strip()
    apelido = entry_apelido.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    morada = entry_morada.get().strip()
    codigo_postal = entry_codigo_postal.get().strip()
    localidade = entry_localidade.get().strip()
    pais = entry_pais.get().strip()

    # Validações dos campos obrigatórios
    if not nome or not apelido or not email or not telefone or not morada or not codigo_postal:
        messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser preenchidos!")
        return

    # Validação de email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Erro", "O email não é válido!")
        return

    # Validação de telefone
    if not telefone.isdigit() or len(telefone) < 9:
        messagebox.showerror("Erro", "O telefone deve conter apenas números e ter pelo menos 9 dígitos!")
        return

    # Inserir dados na base de dados tstore
    try:
        # Conectar ao banco de dados
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tstore"
        )
        mycursor = mydb.cursor()  # Cria um cursor para executar comandos SQL

        # Query de inserção corrigida (garantindo que 'País' seja o nome correto da coluna)
        sql = "INSERT INTO Clientes (Nome, Apelido, Email, Telefone, Morada, Codigo_postal, Localidade, País) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, apelido, email, telefone, morada, codigo_postal, localidade, pais)

        mycursor.execute(sql, valores)
        mydb.commit()  # Confirma a inserção

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

        # Limpar os campos no interface gráfico
        entry_nome.delete(0, tk.END)
        entry_apelido.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_morada.delete(0, tk.END)
        entry_codigo_postal.delete(0, tk.END)
        entry_localidade.delete(0, tk.END)
        entry_pais.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao inserir os dados: {err}")

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()


# Criar a interface gráfica
janela = tk.Tk()
janela.title("INSERIR DADOS - TABELA CLIENTES")
janela.geometry("700x600")
janela.configure(bg="darkblue")
janela.wm_attributes('-alpha', 0.9)  # Janela semi-transparente

# Títulos
titulo = tk.Label(janela, text="Inserir Dados - Clientes", font=("Verdana", 14, "bold"), fg="white", bg="darkblue")
titulo.grid(row=0, column=0, columnspan=2, pady=10)
subtitulo = tk.Label(janela, text="Deve preencher todos os campos", font=("Verdana", 12, "bold"), fg="white", bg="darkblue")
subtitulo.grid(row=1, column=0, columnspan=2, pady=5)


# Função para criar campos de entrada
def criar_campo(rotulo, linha):
    label = tk.Label(janela, text=rotulo, font=("Verdana", 11), fg="white", bg="darkblue")
    label.grid(row=linha, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(janela, width=40)
    entry.grid(row=linha, column=1, padx=10, pady=5, sticky="w")
    return entry


# Criar os campos de entrada
entry_nome = criar_campo("Nome:", 2)
entry_apelido = criar_campo("Apelido:", 3)
entry_email = criar_campo("Email:", 4)
entry_telefone = criar_campo("Telefone:", 5)
entry_morada = criar_campo("Morada:", 6)
entry_codigo_postal = criar_campo("Código Postal:", 7)
entry_localidade = criar_campo("Localidade:", 8)
entry_pais = criar_campo("País:", 9)

# Botão para inserir dados
botao_inserir = tk.Button(janela, text="ENVIAR DADOS", font=("Verdana", 10, "bold"), bg="blue", fg="white", command=inserir_dados)
botao_inserir.grid(row=10, column=0, columnspan=2, pady=20)

# Iniciar a aplicação
janela.mainloop()
