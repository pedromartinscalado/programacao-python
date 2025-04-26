#  Somar os valores de uma lista Validação
while True:
    numeros = []

    for i in range(5):
        while True:
            try:
                num = float(input(f"Digite o {i+1}º número: ").replace(",", "."))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida! Introduza um número válido.")

    print("A soma dos valores é:", sum(numeros))

    repetir = input("Deseja repetir o processo? (S/N): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break