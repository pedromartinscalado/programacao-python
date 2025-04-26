numeros = [2, 5, 8, 11, 14]

numeros.append(20)
numeros[numeros.index(8)] = 9
numeros.pop(0)
print(len(numeros))
