def obter_temperatura():
    while True:
        try:
            return float(input("Digite a temperatura em Celsius: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida! Introduza um número válido.")

def converter_temperatura():
    while True:
        celsius = obter_temperatura()
        fahrenheit = (celsius * 9/5) + 32
        print(f"\nA temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.2f}°F.\n")

        repetir = input("Deseja converter outra temperatura? (s/n): ").strip().lower()
        if repetir != 's':
            print("\nObrigado por utilizar o programa! Lembre-se: o verão está a caminho!")
            break

converter_temperatura()










