# Quiz sobre o Pai Natal

# Listas com perguntas, opções e respostas corretas
perguntas = [
    "Qual é o nome do lugar onde o Pai Natal vive?",
    "Como é chamado o trenó do Pai Natal?",
    "Quantos ajudantes o Pai Natal tem?",
    "Qual é o nome das renas do Pai Natal?",
    "Em que dia o Pai Natal entrega os presentes?"
]

opcoes = [
    ["(a) Polo Norte", "(b) Polo Sul", "(c) Antártida"],
    ["(a) Esquimal", "(b) Rena", "(c) Trenó Mágico"],
    ["(a) 1", "(b) 9", "(c) 12"],
    ["(a) Rudolf, Dancer, Prancer", "(b) Blitz, Vixen, Cupid", "(c) Todas as anteriores"],
    ["(a) 24 de Dezembro", "(b) 25 de Dezembro", "(c) 1 de Janeiro"]
]

respostas_certas = ["a", "c", "b", "c", "a"]  # Respostas corretas para cada pergunta

# Inicializa a pontuação a 0 antes de começar as perguntas
pontuacao_total = 0

# Loop usando while True
i = 0  # Índice para controlar as perguntas
while True:
    # Se chegarmos ao final das perguntas, saímos do loop
    if i >= len(perguntas):
        break

    pergunta = perguntas[i]
    print(f"\n{pergunta}")
    
    # Exibe as opções
    for opcao in opcoes[i]:
        print(opcao)

    # Recebe a resposta do utilizador e remove espaços extras
    resposta = input("Resposta: ").strip().lower()  # .strip() remove espaços extras, .lower() torna tudo minúsculo

    # Verifica se a resposta está correta
    if resposta == respostas_certas[i]:
        print(f"Correto! A resposta é {opcoes[i][ord(respostas_certas[i]) - ord('a')]}. +3 pontos.")
        pontuacao_total += 3
    else:
        print(f"Errado! A resposta correta é {opcoes[i][ord(respostas_certas[i]) - ord('a')]}. 0 pontos.")
    
    i += 1  # Incrementa o índice para a próxima pergunta

# Resultados finais
print(f"\n-- Resultados Finais ---")
print(f"Pontuação total: {pontuacao_total} pontos")
