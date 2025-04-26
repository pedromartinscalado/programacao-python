# Uso de bool para verificar se um número é par
#tentar criar um programa onde possa a validação de dados
#funcao se nao utilizar while true
#validar o numero intero , pode ser 0 , pode ser negativo
#numero = int(input("Insira um número inteiro: "))
#par = (numero % 2 == 0)
#print(f"O número é par? {par}")

def obter_numero_inteiro():
    while True:
        try:
            return int(input("Insira um número inteiro: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

def verificar_par(numero):
    if numero == 0:
        return "Zero é considerado um número par (pois é divisível por 2)."
    return "par" if numero % 2 == 0 else "ímpar"

while True:
    numero = obter_numero_inteiro()
    paridade = verificar_par(numero)
    print(f"O número {numero} é {paridade}.")

    while True:
        repetir = input("Deseja verificar outro número? (S/N): ").strip().lower()
        if repetir in ['s', 'n']:
            break
        print("Resposta inválida! Por favor, insira 'S' para sim ou 'N' para não.")

    if repetir == 'n':
        print("Obrigado por usar o programa! Até breve.")
        break
