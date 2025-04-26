# # Remover um valor da lista
# def obter_numero():
#     while True:
#         try:
#             return int(input("Digite um número inteiro: "))
#         except ValueError:
#             print("Entrada inválida! Introduza um número inteiro.")

# while True:
#     numeros = [obter_numero() for _ in range(5)]

#     remover = obter_numero()

#     if remover in numeros:
#         numeros.remove(remover)
#         print("Lista após remoção:", numeros)
#     else:
#         print("Número não encontrado na lista.")

#     repetir = input("Deseja repetir o processo com uma nova lista? (S/N): ").strip().lower()
#     if repetir != 's':
#         print("Obrigado por usar o programa!")
#         break

def obter_numero():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

while True:
    qtd_numeros = int(input("Quantos números deseja inserir na lista? "))
    numeros = [obter_numero() for _ in range(qtd_numeros)]

    print("Lista inicial:", numeros)

    remover = obter_numero()

    if remover in numeros:
        numeros.remove(remover)
        print(f"Lista após remoção do número {remover}:", numeros)
    else:
        print(f"Número {remover} não encontrado na lista.")

    repetir = input("Deseja repetir o processo com uma nova lista? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break
