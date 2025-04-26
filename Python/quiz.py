## Quiz sobre hábitos saudáveis
##
## Pergunta 1
##print("Quanto tempo de exercício devemos praticar por dia? (Escolhe uma letra)")
##print("(a) 10 minutos")
##print("(b) 30 minutos")
##print("(c) 1 hora")
##resposta1 = input("Resposta: ").lower()
##
##condição simples
##if resposta1 != "b":
##    pontos1 = 0
##    print("Errado! A resposta é 30 minutos. 0 pontos.")
##else:
##    pontos1 = 3
##    print("Certo. 3 pontos.")
##
##
##
############################################################
## Pergunta 2
##print("\nQual o nome do animal que simboliza o Natal? (Escolhe uma letra)")
##print("(a) Rena")
##print("(b) Elefante")
##print("(c) Tigre")
##
##
##resposta2 = input("Resposta: ").lower()
##if resposta2 == "a":
##    pontos2 = 3
##    print("Correto! A resposta é Rena. +3 pontos.")
##else:
##    pontos2 = 0
##    print("Errado! A resposta correta é Rena. 0 pontos.")
##
## Pergunta 3
##print("\nQuantos copos de água devemos beber por dia? (Escolhe uma letra)")
##print("(a) 1 a 2 copos")
##print("(b) 5 a 6 copos")
##print("(c) 8 a 10 copos")
##resposta3 = input("Resposta: ").lower()
##
##if resposta3 == "c":
##    pontos3 = 3
##    print("Correto! A resposta é 8 a 10 copos. +3 pontos.")
##else:
##    pontos3 = 0
##    print("Errado! A resposta correta é 8 a 10 copos. 0 pontos.")
##
## Pergunta 4
##print("\nQual é a melhor forma de evitar o sedentarismo? (Escolhe uma letra)")
##print("(a) Dormir mais")
##print("(b) Fazer exercícios físicos regularmente")
##print("(c) Comer de forma saudável")
##resposta4 = input("Resposta: ").lower()
##
##if resposta4 == "b":
##    pontos4 = 3
##    print("Correto! A resposta é Fazer exercícios físicos regularmente. +3 pontos.")
##else:
##    pontos4 = 0
##    print("Errado! A resposta correta é Fazer exercícios físicos regularmente. 0 pontos.")
##
## Calculando a pontuação total
##pontuacao_total = pontos1 + pontos2 + pontos3 + pontos4
##
##print(f"\nFim do quiz! Sua pontuação total é: {pontuacao_total} pontos.")








# Quiz sobre hábitos saudáveis

# Pergunta 1
print("Qual a data tradicional do Dia dos Reis? (Escolhe uma letra)")
print("(a) 25 de Dezembro")
print("(b) 6 de Janeiro")
print("(c) 1 de Janeiro")
resposta1 = input("Resposta: ").lower()

if resposta1 == "b":
    pontos1 = 3
    print("Correto! A resposta é 6 de Janeiro. +3 pontos.")
else:
    pontos1 = 0
    print("Errado! A resposta correta é 6 de Janeiro. 0 pontos.")

# Pergunta 2
print("\nQual o nome do animal que simboliza o Natal? (Escolhe uma letra)")
print("(a) Rena")
print("(b) Elefante")
print("(c) Tigre")
resposta2 = input("Resposta: ").lower()

if resposta2 == "a":
    pontos2 = 3
    print("Correto! A resposta é Rena. +3 pontos.")
else:
    pontos2 = 0
    print("Errado! A resposta correta é Rena. 0 pontos.")

# Pergunta 3
print("\nQual é o nome do personagem principal da história do Natal? (Escolhe uma letra)")
print("(a) Elfo")
print("(b) Jesus")
print("(c) Pai Natal")
resposta3 = input("Resposta: ").lower()

if resposta3 == "b":
    pontos3 = 3
    print("Correto! A resposta é Jesus. +3 pontos.")
else:
    pontos3 = 0
    print("Errado! A resposta correta é Jesus. 0 pontos.")

# Soma da pontuação total
pontuacao_total = pontos1 + pontos2 + pontos3

# Resultados finais
print(f"\n-- Resultados Finais ---")
print(f"Pontuação total: {pontuacao_total} pontos")
