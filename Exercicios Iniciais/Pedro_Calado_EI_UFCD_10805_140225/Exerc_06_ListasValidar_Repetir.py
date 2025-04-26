# # Criar uma lista com validação e possibilidade de repetição
# def obter_numero():
#     while True:
#         try:
#             return int(input("Digite um número inteiro: "))
#         except ValueError:
#             print("Entrada inválida! Introduza um número inteiro.")

# while True:
#     numeros = []

#     for i in range(5):
#         num = obter_numero()
#         numeros.append(num)

#     print("Lista final:", numeros)

#     repetir = input("Deseja criar outra lista? (S/N): ").strip().lower()
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
    try:
        qtd = int(input("Quantos números deseja inserir na lista? "))
        if qtd <= 0:
            print("O número de elementos deve ser maior que zero.")
            continue
    except ValueError:
        print("Entrada inválida! Introduza um número inteiro.")
        continue

    numeros = []

    for i in range(qtd):
        num = obter_numero()
        numeros.append(num)

    print(f"Lista final: {numeros}")

    repetir = input("Deseja criar outra lista? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break