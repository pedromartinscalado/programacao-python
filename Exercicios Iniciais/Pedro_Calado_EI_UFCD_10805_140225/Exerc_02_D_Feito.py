def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def calcular_media():
    while True:
        n1 = obter_numero("Digite o primeiro número: ")
        n2 = obter_numero("Digite o segundo número: ")
        n3 = obter_numero("Digite o terceiro número: ")
        
        media = (n1 + n2 + n3) / 3
        print(f"\nA média dos números {n1}, {n2} e {n3} é: {media:.2f}\n")

        repetir = input("Deseja calcular outra média? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado para outras coisas procura-me nas redes sociais!")
            break

calcular_media()












