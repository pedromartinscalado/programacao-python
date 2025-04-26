def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def obter_quantidade(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("A quantidade deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Introduza um número inteiro.")

#app loop ou gameloop
def calcular_total():
    while True:
        # Obtém o preço do produto
        preco_produto = obter_valor("Qual o preço do produto? ")
        
        # Obtém a quantidade desejada
        quantidade = obter_quantidade("Qual a quantidade desejada? ")
        
        # Calcula o total
        total = preco_produto * quantidade
        
        # Exibe o valor total
        print(f"\nPreço do produto: {preco_produto:.2f} Euros")
        print(f"Quantidade desejada: {quantidade}")
        print(f"O total da compra é: {total:.2f} Euros")
        
        # Pergunta se deseja realizar outro cálculo
        repetir = input("Deseja realizar novo cálculo? (S/N): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa! Até breve")
            break

# Executar o programa
calcular_total()

