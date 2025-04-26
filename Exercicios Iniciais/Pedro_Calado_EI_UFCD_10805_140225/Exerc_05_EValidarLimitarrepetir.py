# Somar números até o utilizador digitar 0 (while)
def obter_numero():
    while True:
        try:
            num = float(input("Digite um número entre -10 e 10 (0 para sair): ").replace(",", "."))
            if -10 <= num <= 10:
                return num
            else:
                print("O número deve estar entre -10 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

while True:
    soma = 0
    num = obter_numero()

    while num != 0:
        soma += num
        num = obter_numero()

    print("A soma total é:", soma)

    repetir = input("Deseja realizar outra soma? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break