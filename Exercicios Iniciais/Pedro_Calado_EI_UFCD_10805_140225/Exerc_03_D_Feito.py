while True:
    pergunta1 = input("Qual o nome do colaborador? ")
    pergunta2 = input("Qual a sua cor favorita? ")
    pergunta3 = input("Que comida prefere? ")

    print(f"\nOlá, {pergunta1}!")
    print(f"A sua cor favorita é {pergunta2}.")
    print(f"E parece que adora comer {pergunta3}!\n")

    repetir = input("Deseja repetir? (s/n): ").strip().lower()
    if repetir != 's':
        print("\nMuito obrigado pela sua participação! Até à próxima!")
        break














