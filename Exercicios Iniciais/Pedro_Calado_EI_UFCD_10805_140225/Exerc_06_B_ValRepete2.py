# # Remover um valor da lista
# while True:
#     numeros = []

#     while len(numeros) < 5:
#         try:
#             if len(numeros) == 0:
#                 num = int(input("Digite um número inteiro: "))
#             else:
#                 num = int(input("Digite outro número inteiro: "))
#             numeros.append(num)
#         except ValueError:
#             print("Entrada inválida! Introduza um número inteiro.")

#     print("Lista criada:", numeros)

#     while True:
#         try:
#             remover = int(input("Qual número deseja remover da lista? "))

#             if remover in numeros:
#                 numeros.remove(remover)
#                 print("Lista após remoção:", numeros)
#                 break
#             else:
#                 print("Número não encontrado na lista. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida! Introduza um número inteiro.")

#     repetir = input("Deseja repetir o processo com uma nova lista? (S/N): ").strip().lower()
#     if repetir != 's':
#         print("Obrigado por usar o programa!")
#         break

while True:
    numeros = []

    # Inserção de 5 números
    while len(numeros) < 5:
        try:
            num = int(input(f"Digite o {len(numeros) + 1}º número inteiro: "))
            numeros.append(num)
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

    print("Lista criada:", numeros)

    # Remoção de um número
    while True:
        try:
            remover = int(input("Qual número deseja remover da lista? "))

            if remover in numeros:
                numeros.remove(remover)
                print(f"Lista após remoção do número {remover}:", numeros)
                break
            else:
                print("Número não encontrado na lista. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

    # Repetir o processo
    repetir = input("Deseja repetir o processo com uma nova lista? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break