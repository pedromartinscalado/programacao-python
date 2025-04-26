import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Função para obter todas as bases de dados existentes
def obter_base():
    try:
        # Conexão com o MySQL
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='' 
        )
        
        cursor_inicial = conexao_inicial.cursor()
        cursor_inicial.execute("SHOW DATABASES")
        bases = cursor_inicial.fetchall()
        conexao_inicial.close()
        
        # Preencher o Listbox com as bases de dados
        listbox_base.delete(0, tk.END)  # Limpar o Listbox antes de adicionar
        for base in bases:
            listbox_base.insert(tk.END, base[0])  # Inserir o nome da base de dados

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao obter bases de dados: {err}")

# Função para apagar a base de dados selecionada
def apagar_base():
    base_selecionada = listbox_base.curselection()
    if not base_selecionada:
        messagebox.showwarning("Atenção", "Por favor, selecione uma base de dados para apagar.")
        return
    
    nome_base = listbox_base.get(base_selecionada)  
    
    try:
        # Conexão inicial para apagar a base de dados
        conexao_inicial = mysql.connector.connect(
            host='localhost',
            user='root',  
            password=''  
        )
        
        cursor_inicial = conexao_inicial.cursor()
        cursor_inicial.execute(f"DROP DATABASE IF EXISTS {nome_base}")  
        cursor_inicial.close()
        conexao_inicial.close()

        messagebox.showinfo("Sucesso", f"Base de dados '{nome_base}' apagada com sucesso!")
        obter_base()  # Atualizar a lista de bases de dados

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao apagar a base de dados: {err}")

# Criar a janela principal
root = tk.Tk()
root.title("Gestão de Bases de Dados")

# Configurar o tamanho da janela
root.geometry("400x400")

# Criar uma Label
label_instrucoes = tk.Label(root, text="Selecione uma base de dados para apagar:")
label_instrucoes.pack(pady=10)

# Criar o Listbox para mostrar as bases de dados
listbox_base = tk.Listbox(root, height=10, width=30)
listbox_base.pack(pady=10)

# Criar o botão para apagar a base de dados selecionada
btn_apagar = tk.Button(root, text="Apagar Base de Dados", command=apagar_base, width=20)
btn_apagar.pack(pady=10)

# Criar o botão para obter as bases de dados
btn_obter_base = tk.Button(root, text="Mostrar Bases de Dados", command=obter_base, width=20)
btn_obter_base.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()

