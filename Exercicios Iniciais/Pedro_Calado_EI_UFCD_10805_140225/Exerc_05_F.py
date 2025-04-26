# Pedir senha até estar correta (while)
senha_correta = "python123"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta, tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido!")