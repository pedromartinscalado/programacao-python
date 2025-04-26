while True:
    try:
        num = int(input("Introduza um número: "))

        if num > 0:
            print(f"O número {num} é positivo.")
        elif num < 0:
            print(f"O número {num} é negativo.")
        else:
            print(f"O número é zero.")

    except ValueError:
        print("Entrada inválida! Introduza um número inteiro.")

    while True:
        repetir = input("Deseja verificar outro número? (s/n): ").strip().lower()
        if repetir in ['s', 'n']:
            break
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

    if repetir != 's':
        print("Obrigado por usar o programa!")
        break
