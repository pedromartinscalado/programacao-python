def obter_nome():
    while True:
        nome = input("Digite o seu nome: ").strip()
        
        if len(nome) < 2:
            print("O nome deve ter pelo menos duas letras. Tente novamente.")
        elif any(char.isdigit() for char in nome):
            print("O nome não pode conter números. Tente novamente.")
        elif "@" in nome:
            print("O nome não pode conter '@'. Tente novamente.")
        else:
            return nome

def saudar():
    while True:
        nome = obter_nome()
        print(f"Olá, {nome}! Bem-vindo ao mundo do Python.")
        
        repetir = input("Deseja inserir outro nome? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado e até à próxima!")
            break
saudar()













