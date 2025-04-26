def obter_nome(mensagem):
    while True:
        nome = input(mensagem)
        if any(char.isdigit() for char in nome):  # Verifica se há números no nome
            print("O nome não pode conter números. Tente novamente.")
        else:
            return nome

# Obter nome e sobrenome
nome = obter_nome("Insira o seu nome: ")
sobrenome = obter_nome("Insira o seu sobrenome: ")

# Concatenar e mostrar o nome completo
nome_completo = nome + " " + sobrenome
print(f"\nBem vindo(a): {nome_completo}")
