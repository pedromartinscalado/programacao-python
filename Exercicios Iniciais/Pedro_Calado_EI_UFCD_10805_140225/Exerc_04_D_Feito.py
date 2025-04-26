# Comparação de três números
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def encontrar_maior():
    while True:
        a = obter_numero("Digite o primeiro número: ")
        b = obter_numero("Digite o segundo número: ")
        c = obter_numero("Digite o terceiro número: ")

        maior = max(a, b, c)
        if maior == a:
            print(f"O maior número é: {a} (Primeiro número)")
        elif maior == b:
            print(f"O maior número é: {b} (Segundo número)")
        else:
            print(f"O maior número é: {c} (Terceiro número)")

        repetir = input("Deseja verificar outros números? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa!")
            break
encontrar_maior()



