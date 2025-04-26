# #  Criar uma lista de nomes e verificar se um nome está nela
# nomes = [input("Digite um nome: ") for _ in range(5)]
# procurado = input("Digite um nome para verificar se está na lista: ")

# if procurado in nomes:
#     print(f"{procurado} está na lista!")
# else:
#     print(f"{procurado} não foi encontrado.")


def obter_nome():
    while True:
        nome = input("Digite um nome: ").strip()
        if len(nome) == 0 or any(char.isdigit() for char in nome):
            print("Nome inválido! Não pode ser vazio ou conter números.")
        else:
            return nome

# Usando a função
nomes = [obter_nome() for _ in range(5)]
procurado = input("Digite um nome para verificar se está na lista: ")

if procurado in nomes:
    print(f"{procurado} está na lista!")
else:
    print(f"{procurado} não foi encontrado.")