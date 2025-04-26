# #Conversão de números em strings
# numero = 25.6
# numero_str = str(numero)
# print("O número " + numero_str + " agora é uma string!")

# Conversão de um número em string
def obter_numero():
    while True:
        try:
            numero = float(input("Insira um número: "))
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

numero = obter_numero()
numero_str = str(numero)

print(f"O número {numero_str} agora é uma string!") 
