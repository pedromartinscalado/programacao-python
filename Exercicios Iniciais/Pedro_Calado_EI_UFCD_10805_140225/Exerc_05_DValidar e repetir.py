# Contagem regressiva com interação
def obter_numero():
    while True:
        try:
            num = int(input("Digite um número inteiro para iniciar a contagem regressiva: "))
            if num < 0:
                print("O número deve ser zero ou positivo. Tente novamente.")
            else:
                return num
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

while True:
    num = obter_numero()

    while num >= 0:
        print(num)
        num -= 1

    print("FIM!")

    repetir = input("Deseja fazer outra contagem regressiva? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break