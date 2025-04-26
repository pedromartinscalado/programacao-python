from tkinter import * #Importar biblioteca
 
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))
 
def button_clear():
    display.delete(0, END)
 
def button_add():
    first_number = display.get()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_number)
    display.delete(0, END)
 
def button_subtract():
    first_number = display.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = float(first_number)
    display.delete(0, END)
 
def button_multiply():
    first_number = display.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    display.delete(0, END)
 
def button_divide():
    first_number = display.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_number)
    display.delete(0, END)
 
def button_equal():
    second_number = display.get()
    display.delete(0, END)
    if operation == "addition":
        display.insert(0, f_num + float(second_number))
    elif operation == "subtraction":
        display.insert(0, f_num - float(second_number))
    elif operation == "multiplication":
        display.insert(0, f_num * float(second_number))
    elif operation == "division":
        if float(second_number) == 0:
            display.insert(0, "Erro: Não é possível divisão por zero")
        else:
           display.insert(0, f_num / float(second_number))
 
window = Tk()
window.title("Calculadora")
 
display = Entry(window, width=35, borderwidth=3)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=40)
 
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
 
button_add = Button(window, text="+", padx=39, pady=20, bg="lightblue", command=button_add)
button_subtract = Button(window, text="-", padx=41, pady=20, bg="lightgreen", command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, bg="lightcoral", command=button_multiply)
button_divide = Button(window, text="/", padx=41, pady=20, bg="lightgoldenrod", command=button_divide)
button_equal = Button(window, text="CALCULAR",padx=63, pady=20, bg="lightpink", command=button_equal)
button_clear = Button(window, text="Clear", padx=79, pady=20, bg="lightgray", command=button_clear)
 
# Layout dos botões
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
 
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
 
 
window.mainloop()
