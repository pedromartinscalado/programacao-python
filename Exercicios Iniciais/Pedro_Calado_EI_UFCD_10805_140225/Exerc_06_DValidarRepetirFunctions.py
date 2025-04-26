#  Somar os valores de uma lista Validação
def obter_numero():
    while True:
        try:
            return float(input("Digite um número: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def somar_lista():
    numeros = [obter_numero() for _ in range(5)]
    print("A soma dos valores é:", sum(numeros))

while True:
    somar_lista()

    repetir = input("Deseja repetir o processo? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break