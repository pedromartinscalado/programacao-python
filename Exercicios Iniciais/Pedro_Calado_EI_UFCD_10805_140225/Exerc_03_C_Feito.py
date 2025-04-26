def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if len(texto) < 1:
            print("A entrada deve ter pelo menos uma letra. Tente novamente.")
        elif any(char.isdigit() for char in texto):
            print("A entrada não pode conter números. Tente novamente.")
        else:
            return texto

def guardar_dados():
    while True:
        nome = obter_texto("Nome: ")
        cidade = obter_texto("Cidade: ")
        profissao = obter_texto("Profissão: ")

        print(f"\nAqui está a sua frase dinâmica:\n{nome} mora em {cidade} e trabalha como {profissao}.\n")

        repetir = input("Deseja inserir outros dados? (s/n): ").strip().lower()
        if repetir != 's':
            print("\nMuito obrigado por usar o programa! Até à próxima!")
            break

guardar_dados()















