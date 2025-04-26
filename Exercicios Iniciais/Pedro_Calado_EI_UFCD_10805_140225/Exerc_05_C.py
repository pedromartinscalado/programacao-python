# Percorrer uma lista de nomes (for)
def obter_nome():
    while True:
        nome = input("Digite um nome: ").strip()
        if len(nome) < 1:
            print("O nome deve ter pelo menos uma letra. Tente novamente.")
        elif any(char.isdigit() for char in nome):
            print("O nome não pode conter números. Tente novamente.")
        else:
            return nome

while True:
    try:
        qtd_nomes = int(input("Quantos nomes deseja inserir? "))
        if qtd_nomes <= 0:
            print("O número deve ser maior que zero. Tente novamente.")
            continue
    except ValueError:
        print("Entrada inválida! Introduza um número inteiro.")
        continue

    nomes = [obter_nome() for _ in range(qtd_nomes)]

    for nome in nomes:
        print("Olá,", nome)

    repetir = input("Deseja inserir outra lista de nomes? (s/n): ").strip().lower()
    if repetir != 's':
        print("Obrigado por usar o programa!")
        break