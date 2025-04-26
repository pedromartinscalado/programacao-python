
while True:
    nome_livro = input("Qual é o nome do livro? ").strip()
    if nome_livro:  # Verifica se o nome não está vazio
        break
    print("O nome do livro não pode estar vazio. Tente novamente.")


while True:
    try:
        preco = float(input("Qual é o preço do produto? ").replace(",", "."))
        if preco <= 0:
            print("O preço não pode ser zero ou negativo. Tente novamente.")
            continue
        if round(preco, 2) != preco:
            print("O preço não pode ter mais de duas casas decimais. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Introduza um número válido.")


while True:
    try:
        quantidade = int(input("Qual é a quantidade desejada? "))
        if quantidade <= 0:
            print("A quantidade deve ser um número inteiro positivo maior que zero. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Introduza um número inteiro válido.")


print(f"\nO nome do livro é: {nome_livro}, O Preço do livro é: {preco:.2f}€, A Quantidade desejada é: {quantidade}, O Total a pagar é: {preco * quantidade:.2f}€")
