# Contar quantas vezes um número aparece na lista
numeros = [int(input("Digite um número: ")) for _ in range(5)]
procurado = int(input("Digite um número para contar na lista: "))

print(f"O número {procurado} aparece {numeros.count(procurado)} vezes na lista.")