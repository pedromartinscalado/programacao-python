def obter_palavra():
    while True:
        palavra = input("Digite uma palavra: ").strip()
        if not palavra.isalpha():
            print("A palavra deve conter apenas letras. Tente novamente.")
        else:
            return palavra

def obter_numero():
    while True:
        try:
            vezes = int(input("Quantas vezes quer repetir? "))
            if vezes <= 0:
                print("O número deve ser maior que zero. Tente novamente.")
            else:
                return vezes
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro válido.")

def repetir_palavra():
    while True:
        palavra = obter_palavra()
        vezes = obter_numero()
        print(f"\nAqui está a palavra repetida {vezes} vezes:")
        print((palavra + " ") * vezes)  # Adiciona o espaço após cada repetição

        repetir = input("\nDeseja repetir outra palavra? (s/n): ").strip().lower()
        if repetir != 's':
            print("\nObrigado por usar o programa! Até a próxima!")
            break

repetir_palavra()

















