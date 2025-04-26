# # Pedir user e password até ambos estarem corretas (while)
# user_c1 = "admin"
# user_c2 = "ADMIN"
# password_c = ""

# while True:
#     username = input("Digite o username: ").strip()
#     password = input("Digite a password: ")

#     if (username == user_c1 or username == user_c2) and password == password_c:
#         print("Acesso permitido!")
#         break
#     else:
#         print("Username ou password incorretos, tente novamente.")

user_c1 = "admin"
user_c2 = "ADMIN"
password_c = ""

tentativas = 3  # Definir o número de tentativas permitidas

while tentativas > 0:
    username = input("Digite o username: ").strip()
    password = input("Digite a password: ")

    if (username == user_c1 or username == user_c2) and password == password_c:
        print("Acesso permitido!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Username ou password incorretos. Você tem {tentativas} tentativas restantes.")
        else:
            print("Número de tentativas excedido. Acesso bloqueado.")