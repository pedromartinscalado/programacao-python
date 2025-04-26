# Dicionário para mapear os meses aos seus números correspondentes
ordem_meses = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
}

# Lista para armazenar os meses inseridos pelo utilizador
meses = []

# Pedir ao utilizador para inserir três meses
for i in range(3):
    while True:
        mes = input(f"Digite o {i+1}º mês: ").strip().lower()  # Tornar a entrada minúscula
        if mes in ordem_meses:
            meses.append(mes)
            break
        else:
            print("Mês inválido. Tente novamente com um mês válido (ex: janeiro, fevereiro, ...).")

# Ordenar os meses pela ordem do calendário
meses.sort(key=lambda mes: ordem_meses[mes])

# Apresentar a lista ordenada
print("Meses ordenados:", meses)