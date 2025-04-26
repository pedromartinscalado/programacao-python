def obter_numero():    
    while True:
        try:
            numero = int(input("Insira um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

def verificar_paridade():    
    while True:
        numero = obter_numero()
        par = (numero % 2 == 0)
        print(f"O número {numero} é par? {par}")

        while True:  # Ciclo para garantir que a resposta seja válida
            repetir = input("Deseja verificar outro número? (s/n): ").strip().lower()
            if repetir in ['s', 'n']:  # Aceita apenas 's' ou 'n'
                break
            print("Resposta inválida! Por favor, insira 's' para sim ou 'n' para não.")

        if repetir != 's':
            print("Obrigado por usar o programa!")
            break

# Executar o programa
verificar_paridade()



