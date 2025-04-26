def obter_numero():
    while True:
        try:
            return float(input("Digite um número: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def calcular_quadrado():
    while True:
        num = obter_numero()
        quadrado = num ** 2
        print(f"O quadrado de {num:.2f} é: {quadrado:.2f}")

        repetir = input("Deseja calcular o quadrado de outro número? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa!")
            break

calcular_quadrado()







