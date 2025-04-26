def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def calcular_soma():
    while True:

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")


        soma = num1 + num2
        print(f"A soma é: {soma:.2f}")


        repetir = input("Deseja realizar outra soma? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa!")
            break

calcular_soma()








