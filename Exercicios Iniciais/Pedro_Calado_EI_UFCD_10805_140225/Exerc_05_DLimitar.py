# Contagem regressiva com interação limitada
def obter_numero():
    while True:
        try:
            num = int(input("Digite um número inteiro entre 1 e 30: "))
            if 1 <= num <= 30:
                return num
            else:
                print("O número deve estar entre 1 e 30. Tente novamente.")
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