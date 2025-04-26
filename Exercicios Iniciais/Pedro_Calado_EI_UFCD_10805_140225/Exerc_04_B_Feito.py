# Determinar a maior de duas idades
while True:
    try:
        idade1 = int(input("Digite a primeira idade: "))
        idade2 = int(input("Digite a segunda idade: "))
        
        # Garantir que as idades não sejam negativas
        if idade1 < 0 or idade2 < 0:
            print("A idade não pode ser negativa. Tente novamente.")
            continue

        if idade1 > idade2:
            print("A primeira pessoa é mais velha.")
        elif idade1 < idade2:
            print("A segunda pessoa é mais velha.")
        else:
            print("Ambas têm a mesma idade.")

    except ValueError:
        print("Entrada inválida! Introduza um número inteiro.")

    repetir = input("Deseja comparar outras idades? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break

