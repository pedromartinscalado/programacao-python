def obter_numero(mensagem):
    while True:
        try:
            
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")


num1 = obter_numero("Digite o primeiro número: ")
num2 = obter_numero("Digite o segundo número: ")


soma = num1 + num2

print(f"A soma de {num1} e {num2} é: {soma}")



