def obter_valor(mensagem, tipo=float):
    """Obtém um valor numérico válido do utilizador, garantindo que seja positivo."""
    while True:
        try:
            valor = tipo(input(mensagem).replace(",", "."))  # Permite vírgula como separador decimal
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

while True:
  
    preco_produto = obter_valor("Qual é o preço do produto? ")
    quantidade = obter_valor("Qual é a quantidade desejada? ", int)  # Quantidade inteira

    total = preco_produto * quantidade


    print(f"\nO total da compra é: {total:.2f} Euros")

   
    repetir = input("\nDeseja calcular outra compra? (S/N): ").strip().lower()
    if repetir != 's':
        print("\nObrigado por usar o programa! Até breve.")
        break

