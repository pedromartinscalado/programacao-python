
pip install customtkinter


import customtkinter as ctk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Não é possível dividir por zero"
    return x / y

def power(x, y):
    return math.pow(x, y)

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        elif operation == '5':
            result = power(num1, num2)
        else:
            result = "Operação inválida"

        label_result.config(text=f"Resultado: {result}")
    except ValueError:
        label_result.config(text="Erro: Entrada inválida")

# Configuração da janela principal
root = ctk.CTk()
root.title("Calculadora Personalizada")
root.geometry("400x500")

# Variável para armazenar a operação selecionada
operation_var = ctk.StringVar(value='1')

# Widgets da interface gráfica
label_num1 = ctk.CTkLabel(root, text="Digite o primeiro número:")
label_num1.pack(pady=10)

entry_num1 = ctk.CTkEntry(root)
entry_num1.pack(pady=10)

label_num2 = ctk.CTkLabel(root, text="Digite o segundo número:")
label_num2.pack(pady=10)

entry_num2 = ctk.CTkEntry(root)
entry_num2.pack(pady=10)

label_operation = ctk.CTkLabel(root, text="Selecione a operação:")
label_operation.pack(pady=10)

radio_add = ctk.CTkRadioButton(root, text="Adição", variable=operation_var, value='1')
radio_add.pack(pady=5)

radio_subtract = ctk.CTkRadioButton(root, text="Subtração", variable=operation_var, value='2')
radio_subtract.pack(pady=5)

radio_multiply = ctk.CTkRadioButton(root, text="Multiplicação", variable=operation_var, value='3')
radio_multiply.pack(pady=5)

radio_divide = ctk.CTkRadioButton(root, text="Divisão", variable=operation_var, value='4')
radio_divide.pack(pady=5)

radio_power = ctk.CTkRadioButton(root, text="Exponenciação", variable=operation_var, value='5')
radio_power.pack(pady=5)

button_calculate = ctk.CTkButton(root, text="Calcular", command=calculate)
button_calculate.pack(pady=20)

label_result = ctk.CTkLabel(root, text="Resultado: ")
label_result.pack(pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
