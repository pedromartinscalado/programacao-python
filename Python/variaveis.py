comentario_longo="""a = 456 #inteiro int
b = 123.67 #float float - casas decimais
c = True #False #variavel do tipo verdadeiro ou falso (boleana)
d = "Hello World" #variavel do tipo texto / string / str

#print(str(a)+d) #passa a ser texto
#print (str(a) + " " + d)

#print (234 + 345 + 543)
"""
#print(comentario_longo)


nome = input("Insira o seu nome: ")
idade = int(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso: "))

print(f"o seu nome é: {nome} a sua idade é {idade} e o seu peso é {peso} quilos")


def identificar():
    #print(f"o seu nome é {nome} a sua idade é {idade} anos e o seu peso é {peso} quilos")
#   global nome
    print("O seu nome é: ", nome)
    identificar()

#global
