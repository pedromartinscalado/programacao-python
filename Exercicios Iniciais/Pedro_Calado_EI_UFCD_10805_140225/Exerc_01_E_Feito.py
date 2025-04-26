idade1 = 18
idade2 = 21

# Comparar se ambos são maiores de idade
maior_de_idade1 = idade1 >= 18
maior_de_idade2 = idade2 >= 18

print(f"A pessoa 1 (idade {idade1}) é maior de idade? {maior_de_idade1}")
print(f"A pessoa 2 (idade {idade2}) é maior de idade? {maior_de_idade2}")

# Verificar se ambas são maiores de idade
ambos_maiores = maior_de_idade1 and maior_de_idade2
print("Ambos são maiores de idade?", ambos_maiores)

