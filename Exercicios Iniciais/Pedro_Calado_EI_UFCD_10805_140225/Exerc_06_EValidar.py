# #  Criar uma lista de nomes, verificar se um nome está nela e fazer validação
# def obter_nome():
#     while True:
#         nome = input("Digite um nome: ").strip()
#         if len(nome) > 1 and not any(char.isdigit() or char == "@" for char in nome):
#             return nome
#         print("Nome inválido! Deve conter mais de uma letra, não pode ter números nem '@'. Tente novamente.")

# while True:
#     nomes = [obter_nome() for _ in range(5)]

#     procurado = input("Digite um nome para verificar se está na lista: ").strip()

#     if procurado in nomes:
#         print(f"{procurado} está na lista!")
#     else:
#         print(f"{procurado} não foi encontrado.")

#     print("Lista final de nomes:", nomes)

#     repetir = input("Deseja repetir o processo? (S/N): ").strip().lower()
#     if repetir != 's':
#         print("Obrigado por usar o programa!")
#         break

def obter_nome():
    while True:
        nome = input("Digite um nome: ").strip()
        if len(nome) > 1 and not any(char.isdigit() or char == "@" for char in nome):
            return nome
        print("Nome inválido! Deve conter mais de uma letra, não pode ter números nem '@'. Tente novamente.")

while True:
    nomes = [obter_nome() for _ in range(5)]

    procurado = input("Digite um nome para verificar se está na lista: ").strip()

    if procurado in nomes:
        print(f"{procurado} está na lista!")
        remover = input(f"Deseja remover {procurado} da lista? (s/n): ").strip().lower()
        if remover == 's':
            nomes.remove(procurado)
            print(f"{procurado} foi removido da lista.")
    else:
        print(f"{procurado} não foi encontrado.")

    print("Lista final de nomes:", nomes)

    repetir = input("Deseja repetir o processo? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break