# Classificação de notas
while True:
    try:
        nota = float(input("Digite a nota do aluno (0 a 10): ").replace(",", "."))
        if nota < 0 or nota > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.")
            continue
        if nota >= 9.5:
            print("Aprovado!")
        else:
            print("Reprovado.")
    except ValueError:
        print("Entrada inválida! Introduza um número válido.")

    repetir = input("Deseja verificar outra nota? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break

