def obter_valor(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def calcular_total():
    while True:
        preco_produto = obter_valor("Qual o preço do produto? ", float)
        
        # Garantir que a quantidade seja um número inteiro
        while True:
            try:
                quantidade = int(input("Qual é a quantidade desejada? "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Introduza um número inteiro para a quantidade.")
        
        total = preco_produto * quantidade
        print(f"O total da compra é: {total:.2f} Euros")
        
        repetir = input("Deseja realizar novo cálculo? (S/N): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa! Até breve.")
            break

# Executar o programa
calcular_total()




