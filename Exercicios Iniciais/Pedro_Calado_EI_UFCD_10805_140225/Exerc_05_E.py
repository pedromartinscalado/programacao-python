# Somar números até o utilizador digitar 0 (while)
soma = 0
num = float(input("Digite um número (0 para sair): "))

while num != 0:
    soma += num
    num = float(input("Digite um número (0 para sair): "))

print("A soma total é:", soma)