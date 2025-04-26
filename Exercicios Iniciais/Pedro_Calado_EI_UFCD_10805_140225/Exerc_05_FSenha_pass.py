# Pedir user e password até ambos estarem corretas (while)
username_correto = "admin"
password_correto = ""

while True:
    username = input("Digite o username: ").strip().lower()
    password = input("Digite a password: ")

    if username == username_correto and password == password_correto:
        print("Acesso permitido!")
        break
    else:
        print("Username ou password incorretos, tente novamente.")