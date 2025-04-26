def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

def calcular_divisao():
    while True:
        dividendo = obter_inteiro("Digite o dividendo: ")
        
        while True:
            divisor = obter_inteiro("Digite o divisor: ")
            if divisor == 0:
                print("O divisor não pode ser zero. Tente novamente.")
            else:
                break

        quociente = dividendo // divisor
        resto = dividendo % divisor
        divisao_exata = dividendo / divisor

        # Exibição dos resultados
        print(f"\nResultado da divisão:")
        print(f"Divisão exata: {divisao_exata:.2f}")
        print(f"Quociente: {quociente}")
        print(f"Resto: {resto}")

        repetir = input("\nDeseja realizar outra divisão? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa!")
            break

calcular_divisao()









