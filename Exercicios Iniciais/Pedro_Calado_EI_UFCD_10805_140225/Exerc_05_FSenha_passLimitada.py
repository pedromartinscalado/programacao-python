# Definindo os valores corretos
user_correto = "admin"
password_correta = "senha123"

while True:
    # Pedir username e password
    username = input("Digite o username: ").strip().lower()  # Tornando o username insensível a maiúsculas
    password = input("Digite a password: ")

    # Verificando se o username e a senha estão corretos
    if username == user_correto and password == password_correta:
        print("Acesso permitido!")
        break  # Interrompe o ciclo se ambos estiverem corretos
    else:
        print("Username ou password incorretos, tente novamente.")