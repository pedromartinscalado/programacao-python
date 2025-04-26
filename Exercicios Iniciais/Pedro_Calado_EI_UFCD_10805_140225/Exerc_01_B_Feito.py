# # Cálculo matemático simples com variáveis (int e float)
# preco_produto = float(input("Qual o preço do produto? "))
# quantidade = float(input("Qual quantidade ou peso desejado? "))
# total = preco_produto * quantidade
# print(f"O total da compra é: {total:.2f} Euros")


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

# Obter os valores
preco_produto = obter_valor("Qual o preço do produto? ")
quantidade = obter_valor("Qual é a quantidade desejada? ", int)  # Garante número inteiro

# Calcular o total
total = preco_produto * quantidade

# Exibir o resultado formatado
print(f"\nO total da compra é: {total:.2f} Euros")
