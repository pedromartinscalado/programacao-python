# # Contar quantas vezes um número aparece na lista Val e repete
# def obter_numero():
#     while True:
#         try:
#             return int(input("Digite um número inteiro: "))
#         except ValueError:
#             print("Entrada inválida! Introduza um número inteiro.")

# while True:
#     numeros = [obter_numero() for _ in range(5)]

#     procurado = obter_numero()

#     print(f"O número {procurado} aparece {numeros.count(procurado)} vezes na lista.")

#     repetir = input("Deseja repetir a contagem com nova lista? (S/N): ").strip().lower()
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

    procurado = obter_numero()

    print(f"O número {procurado} aparece {numeros.count(procurado)} vezes na lista.")

    repetir = input("Deseja repetir a contagem com nova lista? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break
