# # Remover um valor da lista
# numeros = [int(input("Digite um número: ")) for _ in range(5)]
# remover = int(input("Digite um número para remover da lista: "))

# if remover in numeros:
#     numeros.remove(remover)
#     print("Lista após remoção:", numeros)
# else:
#     print("Número não encontrado na lista.")

def obter_numero():
    while True:
        try:
            return int(input("Digite um número: "))
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

while True:
    # Criando a lista com 5 números
    numeros = [obter_numero() for _ in range(5)]
    
    # Solicita o número para remoção
    remover = obter_numero()

    # Remover o número se ele estiver na lista
    if remover in numeros:
        numeros.remove(remover)
        print("Lista após remoção:", numeros)
    else:
        print("Número não encontrado na lista.")

    # Pergunta ao usuário se ele deseja continuar
    repetir = input("Deseja realizar outra remoção? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break