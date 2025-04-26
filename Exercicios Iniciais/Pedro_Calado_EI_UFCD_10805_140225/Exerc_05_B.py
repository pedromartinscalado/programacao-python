#Ciclo for exemplo Tabuada
def obter_numero():
    while True:
        try:
            return int(input("Insira um número inteiro: "))
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

while True:
    num = obter_numero()

    for i in range(1, 11):
        print(f"Tabuada de {num} x {i} = {num * i}")

    repetir = input("Deseja ver a tabuada de outro número? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break