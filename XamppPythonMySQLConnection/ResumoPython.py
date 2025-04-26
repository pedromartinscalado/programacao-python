#Números - Slide 50
#Números são um tipo de dados em Python e podem ser de 3 tipos int, float e
#complex.

#int - números inteiros (-3,0,3)

#float - qualquer número incluindo números com casas decimais
#(-3.2, 4.5)


#complex, são números complexos usados em ciência de dados e estatistica
# engenharia e matemática



#Exemplo de números complexos em Python
##complexo1 = 2 + 3j
##complexo2 = -1 - 2j
####
##print(f"O primeiro número complexo é: {complexo1}")
##print(f"O segundo número complexo é: {complexo2}")
##

### Operações com números complexos
##soma = complexo1 + complexo2
##diferenca = complexo1 - complexo2
##produto = complexo1 * complexo2
##quociente = complexo1 / complexo2
##
##
###Apresentar os resultados no terminal
##print(f"A soma dos números complexos é: {soma}")
##print(f"A diferença entre os números complexos é: {diferenca}")
##print(f"O produto dos números complexos é: {produto}")
##print(f"O quociente dos números complexos é: {quociente} ")
##

####Mais alguns exemplos: - Slide 51
###import math
##print("Raiz quadrada:", math.sqrt((25)) #Raiz quadrada de um número
##print("Potência", 2 ** 5) # Potência (2 elevado a 5)

    
##print("Módulo:", 10 % 3) # Módulo (resto da divisão de 10 por 3)
##print("Divisão inteira:", 17 // 3) # Divisão inteira (resultado da divisão de 17 por 3)

##
##print("Logaritmo natural:", math.log(20)) # Logaritmo natural (log de 20)
##print("Logaritmo base 10:", math.log(100)) # Logaritmo base 10 (log de 100)
##
##print("Seno de 45 graus:", math.sin(math.radians(45))) # Seno de 45 graus (em radianos)
##print("Cosseno de 60 graus:", math.cos(math.radians(60)) # Cosseno de 60 graus
##
##print("Tangente de 30 graus:", math.tan(math.radians(30))) # Tangente de 30 graus
##print("Fatorial de 5:", math.factorial(5)) # Fatorial de um número (5!)
##print("Valor absoluto:", abs(-15)) # Valor absoluto de -15




##Variáveis - Slide 52
##Podemos realizar cálculos diretamente, mas o mais correto é usarmos variáveis.
##As variáveis servem para guardar, editar, atualizar, valores de dados. São essenciais
##em programação e em especial na gestão de bases de dados. As variáveis são
##criadas a partir do momento em que lhe atribuímos um valor e tem uma sintaxe
##do tipo nome = valor, sendo o sinal de igual o sinal de atribuição.

##
##x = 5 # A variável x está a receber o valor inteiro 5
##y = .5 # A variável y está a receber o valor float .5
##multiplicar = x*y
##
##print(f"Se multiplicarmos x por y temos o resultado = ", {multiplicar})

## Slide 53
##Existem regras importantes na criação de variáveis.
##• O nome da variável não pode começar por um número;
##• Não pode usar palavras reservadas (palavras que já têm um significado
##na programação em Python;
##• Não pode usar certos caracteres como acentos, til, c com cedilha, sinais
##de operação, dois pontos, etc;
##• Não podem ser duas palavras separadas (ex: minha var);
##• Para juntar duas palavras no nome usamos o underscore (ex:
##meu_score);
##• O Python é case sensitive (Score não é o mesmo que score);
##• Podemos criar mais do que uma variável na mesma linha com uma
##sintaxe do tipo: a, b. c = 12,4,6

#### Slide 54
####Variáveis
####Algumas curiosidades:
####Não podemos concatenar variáveis de tipos diferentes (ex: numero+string), a
####não ser que seja utilizado um método de conversão.
####O Python lê o código de cima para baixo.
####O Python é uma programação dinâmica e
####forte, podemos atualizar o valor de um dado
####ao longo do programa e não podemos
####misturar diferentes tipos de variáveis.
##
##
####a,b,c =12,4,6
####print ("Soma de a+b+c = ", a+b+c)
####
####a=b=c="Python"
####print (c)
##
##
##a=b=c="Python"
##d='Estamos a aprender '
##print (d+a) #Aqui o + serve para fazer a concatenação das variáveis

## Slide 55
##Variáveis do tipo string
##Uma string é um valor alfanumérico. Para a identificarmos podemos usar aspas
##simples ou aspas duplas.


##nome = "Manuel" #aqui usamos aspas
##apelido = 'Lucas' #aqui usamos plicas
##
##print (nome, apelido)
##
##print (nome+apelido)



## Slide 56
##Inserir variáveis dentro de uma mensagem
##Existem várias formas sendo esta a expressão mais comum:
##
##
###variáveis no meio de mensagens com a instrução print
##Nome = "Manuel Joaquim"
##Idade = 37
##Localidade = "Lisboa"
##print(f"O {Nome}, tem {Idade} anos e vive em {Localidade}")
##
##Resultado na consola:
##"O Manuel Joaquim, tem 37 anos e vive em Lisboa"

#### Slide 57
####Outras formas menos comuns, que exemplificam a vantagem de usar a
####instrução f antes das aspas “ ” ou plicas ‘ ‘
##
##
### Inserção de Variáveis em Strings nome = "João"
##idade = 30
##print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
##
##
##
### Identificação de Placeholders por Nome
##nome = "Ana"
##cidade = "Lisboa"
##print("Olá, meu nome é (nome} e eu moro em {cidade}.".format(nome=nome, cidade=cidade))
##
##
##
###Formatação Avançada
##preco 49.99
##print("O preço é {:.2f} Euros".format(preco))
##
##
##
### Uso de Expressões Dentro de Placeholders
##largura = 5
##altura = 10
##print("A área do retângulo é {}".format(largura * altura))



##Variáveis com texto longo - Slide 58
##Os comentários de várias linhas, são úteis, se quisermos comentar
##vários blocos de código, por exemplo para debug, ou se quisermos criar
##comentários longos para explicar o código.
##Utilizados em variáveis são muito úteis quando queremos escrever um
##texto longo, por exemplo apresentar a descirção de um produto.
##
##
##
###Variável com texto longo
##comentar = "Quando queremos usar um texto longo, por exemplo,para fazermos a descrição de um produto, podemos usar 3 aspas ou 3 pelicas, no início e no fim e assim enviar para a base de dados."
##print(comentar)


## - Slide 59
##Exercícios - métodos com Strings
##Em bases de dados usamos muitas vezes variáveis do tipo String, por
##exemplo para adicionarmos o dados relativos a nome, descrição, etc.
##Por isso faz algum sentido começarmos por entender alguns métodos
##que podemos combinar com strings.
##Exercícios - métodos com Strings
##Temos este código:
##
##x = "Técnico/a Especialista em Gestão de Informação e Ciência dos Dados" print("\nCurso de ", x)
##print(f"Texto que vai buscar o conteúdo da variável x: {x}\n")
##
##Perguntas:
##a) O que faz o comando \n no primeiro print?
##b) O que significa o f e a expressão {x} dentro do segundo print?



##Temos este código: Slide 60
##    nome = input("Qual o teu nome?")
##    print("\nOlá, {}!".format(nome))
##Perguntas:
##a) Qual o papel das chavetas e como elas são preenchido com o método
##format().
##b) Como podemos alterar a mensagem para incluir uma segunda variável,
##exemplo:
##curso = "Técnico/a Especialista em Gestão de Informação e Ciência dos
##Dados"?
##Temos este código:
##mensagem = " Olá, Welcome
##print(f"\nMensagem original: '{mensagem}")
##print(f" Mensagem sem espaços em branco: '{mensagem.strip()}"")
##    
##Perguntas:
##a) O que faz o método strip() aplicado à variável mensagem?
##b) O que fazem as aspas simples (') neste exemplo?



##Temos este código: Slide 61
##
##texto = "Programação em Python" print(f"\nTexto original: {texto}")
##print(f"Texto em minúsculas: {texto.lower()}") print(f"Texto em maiúsculas:
##{texto.upper()}")    
##Perguntas:
##a) Qual é a diferença entre os métodos upper() e lower()?
##b) O método upper() modifica permanentemente o conteúdo da variável
##texto?
##Temos este código:
## 
##frase = "Eu gosto muito de programação!"
##print(f" \nFrase original: {frase}")
##print(f"Frase modificada: {frase.replace('gosto', 'adoro)}")   
##Perguntas:
##a) Qual é o objetivo do método replace() neste contexto?
##b) Como podemos substituir múltiplas palavras numa frase?


##
##Exemplo de solução: Slide 62
##    
##frase = """
##Não é fácil apoiar quando não corre bem? Outros iriam desaparecer? Por certo não! Eles não iriam desaparecer. Esta é a diferença!
### Aplicação de múltiplos replaces encadeados frase_corrigida = (frase
##)
##.replace('Não é', 'É') .replace('desaparecer', 'brilhar')
##print(frase_corrigida)
##"""
##Resultado:
##    
##É fácil apoiar quando não corre bem? Outros iriam brilhar? Por certo não!
##Eles não iriam brilhar. Esta é a diferença!




##Temos este código: Slide 63
##   
##texto "Python é incrível" palavras = texto.split() print(texto)
##print(f"Criar lista de palavras a partir da frase: {palavras}") novo_texto = " ".join(palavras)
##print(f"Texto reconstruído: {novo_texto}\n") 
##Perguntas:
##a) Explica o que faz o método split().
##b) O que faz o método join() neste contexto?
##Temos este código:
##    
##frase = "Eu estou a aprender Python!"
##print(f"A frase {frase} contém (len(frase)} caracteres.\n")
##Perguntas:
##a) O que faz o método len() neste caso?
##b) Como alterar o código para contar apenas o número de palavras na frase?



##
##Temos este código: Slide 64
##    
##mensagem = "O Python ajuda-nos a criar interfaces amigáveis para Bases de dados" posicao
##mensagem.find("Python")
##print(f"A palavra 'Python' foi encontrada na posição {posicao}\n.")
##Perguntas:
##a) O que faz o método find() aplicado à variável mensagem?
##b) O que será exibido caso a palavra procurada não seja encontrada?
##Temos este código:
##    
##texto = "python é poderoso."
##print(f"Texto original: {texto}")
##print(f"Texto com a primeira letra maiúscula: {texto.capitalize()}")
##Perguntas:
##a) O que faz o método capitalize()?
##b) Este método altera todas as palavras da frase ou apenas a primeira?




##Temos este código: Slide 65
##    
##texto = "A linguagem Python é popular porque o PYTHON é simples de entender" contador
##=
##texto.lower().count("python") # Converte tudo para minúsculas antes de contar print(f"O texto contém a palavra 'Python' {contador} vezes")
##Perguntas:
##a) O que faz o método count() aplicado à variável contador?
##b) Porque usámos a variável contador neste contexto?
##Temos este código:
##    
##frase = "Python é uma linguagem de programação de alto nível" print(f"A frase começa com 'Python'? {frase.startswith('Python')}") print(f"A frase termina com 'nível'? {frase.endswith('nível')}")
##Perguntas:
##a) O que verifica o método startswith()?
##b) O método endswith() diferencia maiúsculas e minúsculas?



##Exercícios Python e desafios de aplicação. Slide 66

##Apresentar o resultado em várias linhas Slide 67
##
##
##
###Pedir ao utilizador que insira dois números inteiros x = int(input("Digite um número inteiro: "))
##y = int(input("Digite outro número inteiro: "))
##soma x + y
##subtra = x - y multip = x * y
##**
##potencia = X Y
##divisao = x/y
### Quebrar a variável 'resultado' em várias linhas
##resultado = "Soma: {}\nSubtrair: {\nMultiplicar: {}\nPotencia: {}\nDividir: {}".format( soma, subtra, multip, potencia, divisao
##)
##print(resultado)
##
##Para se guardar os resultados das operações entre os números inseridos
##pelo utilizador em várias linhas, usa-se \n para indicar uma nova linha,
##separando cada operação (soma, subtração, multiplicação, potência e
##divisão) para facilitar a leitura.
##A função format() insere os valores calculados na sequência correta
##dentro das chavetas {}.


####Exercício de cálculos com listas e ciclo for Slide 68
####Perguntas:
####a) O que faz o método format() neste
####contexto?
####b) O que acontece se o utilizador não
####responder com um número inteiro?
##
##
### Pedir 2 números inteiros para calcular x= int(input("Digite um número inteiro: ")) y = int(input("Digite outro número inteiro: "))
##soma = x + y
##subt = x - y
##mult = x * y
##potenc = x ** y
##div = X/Y
### Criar lista de resultados
##resultados = [
##]
##"A soma de x + y é: {}".format(soma), "A subtração de x - y é: {}".format(subt), "A multiplicação de x * y é: {}".format(mult), "A potência de x ** y é: {}".format(potenc), "A divisão de x/y é: {}".format(div)
### Apresentar os resultados
##for i in resultados:
##print(i)

##Explicação do código Slide 69
##
### Pedir 2 números inteiros para calcular
##int(input("Digite um número inteiro: "))
##y = int(input("Digite outro número inteiro: "))
##
### Pedir 2 números inteiros para calcular é um comentário. Comentários de uma
##linha em Python começam com # e servem para explicar o que o código faz,
##mas não são executados.
##Pedir o Primeiro Número:
##x = int(input("Digite um número inteiro: "))
##O comando input("Digite um número inteiro: ") mostra uma mensagem ao
##utilizador (Digite um número inteiro: ) e espera que o utilizador insira um valor.


## Slide 70
##O valor introduzido pelo utilizador é inicialmente uma string (texto). Para o
##transformar num número inteiro, usamos int(...).
##x = int(...) guarda o valor convertido na variável x.
##Pedir o Segundo Número:
##y = int(input("Digite outro número inteiro: "))
##Este comando funciona da mesma maneira que o anterior, mas guarda o
##segundo número introduzido na variável y.
##Assim, x e y passam a conter os dois números inteiros introduzidos pelo
##utilizador, e o código está pronto para efetuar operações com esses valores.


## Slide 71
##soma x + y subt = x - y
##mult = x * y
##potenc = x ** y
##div = x / y
##
##Variáveis de cálculo com base nos valores de x e y introduzidos:
##
##
##resultados = [
##]
##"A soma de x + y é: {}".format(soma),
##"A subtração de x - y é: {}".format(subt),
##*
##"A multiplicação de x y é: {}".format(mult),
##"A potência de x ** y é: {}".format(potenc), "A divisão de x/y é: {}".format(div)
##    
##A variável resultados é uma lista. Listas em Python são criadas usando
##colchetes [], e os elementos dentro da lista são separados por vírgulas.
##
##
##Cada elemento da lista resultados é uma string formatada, que contém um
##texto explicativo e o resultado da operação correspondente.


## Slide 72
##Formato das Strings e format(): 
##"Texto {}".format(valor) é uma maneira de inserir valores dentro de uma string.
##O format() é um método de string que permite substituir {} pelo valor
##especificado dentro dos parênteses format(...).
##O format() é um método de string que permite substituir {} pelo valor
##especificado dentro dos parênteses format(...).
##Itens da Lista e Variáveis:
##Cada string explica uma operação, como soma, subtração, multiplicação, etc.,
##e usa format() para inserir o valor calculado anteriormente.


## Slide 73
##Itens Individuais:
##"A soma de x + y é: {}".format(soma):
##Isso cria uma string que diz "A soma de x + y é: " e insere o valor da variável
##soma no lugar de {}.
##O resultado, caso x = 3 e y = 2, seria "A soma de x + y é: 5".
##"A subtração de x - y é: {}".format(subt):
##Similar ao anterior, mostra o valor de subt, resultado da operação x - y.
##"A multiplicação de x * y é: {}".format(mult):
##Exibe o resultado da multiplicação x * y através da variável mult.


## Slide 74
##"A potência de x ** y é: {}".format(potenc):
##Exibe o resultado de x ** y, que representa x elevado à potência y.
##"A divisão de x / y é: {}".format(div):
##Exibe o resultado da divisão x / y usando a variável div.
##Lista resultados Completa:
##Cada string, após ser formatada, torna-se um elemento dentro da lista
##resultados.
##Essa lista armazena as mensagens formatadas, prontas para serem exibidas.


## Slide 75
##Ciclo for
##for i in resultados:
##    print(i)
##
##Esse trecho de código é responsável por apresentar cada um dos resultados
##calculados anteriormente. Vamos ver o que ele faz, passo a passo:

##A linha for i in resultados: inicia um loop for, que percorre cada elemento da
##lista resultados.

##A variável i representa o elemento atual da lista resultados em cada passagem
##do loop.

##Dentro do loop, print(i) imprime o conteúdo de i, ou seja, a mensagem com o
##resultado atual.

##Como o loop for percorre todos os elementos da lista, o print(i) é executado
##para cada mensagem em resultados.


## Slide 76
##O script completo
##
### Pedir 2 números inteiros para calcular x= int(input("Digite um número inteiro: ")) y = int(input("Digite outro número inteiro: "))
##soma = x + y
##subt = x - y
##mult = x * y
##potenc = x ** y
##div = X/Y
### Criar lista de resultados
##resultados = [
##]
##"A soma de x + y é: {}".format(soma), "A subtração de x - y é: {}".format(subt), "A multiplicação de x * y é: {}".format(mult), "A potência de x ** y é: {}".format(potenc), "A divisão de x/y é: {}".format(div)
### Apresentar os resultados
##for i in resultados:
##print(i)


## Slide 77
##O mesmo cálculo com validação de dados
##
##Se o utilizador introduzir valores incorretos, o programa dá erro e já não
##corre. Para permitirmos que o utilizador tenha a possibilidade de introduzir
##os dados corretos, precisamos de usar a validação de dados. Neste
##exemplo precisamos de garantir que os valores introduzidos sejam
##números inteiros.
##Para isso precisamos de criar uma função utilizando um ciclo while True
##(enquanto for verdade).


###Função para verificar se foi introduzido um número inteiro def pede_int(mensagem):
##while True:
##try:
##numero= int(input(mensagem))
##return numero
##except ValueError:
##print("Erro: Digite um número inteiro válido.")



## Slide 78
##Explicação da função
###Função para verificar se foi introduzido um número inteiro
##def pede_int(mensagem):
##while True:
##try:
##numero= int(input(mensagem))
##return numero
##except ValueError:
##print("Erro: Digite um número inteiro válido.")
##
##
##Esta função pede ao utilizador um número inteiro, repetindo o pedido até que
##seja obtida uma entrada válida. A função usa um loop while True para tentar
##converter o input do utilizador num número inteiro com int(input(mensagem)).
##Caso o utilizador insira algo que não seja um número inteiro, ocorre uma
##exceção ValueError, e uma mensagem de erro é apresentada, pedindo que
##seja digitado um valor válido.



## Slide 79
##O mesmo cálculo com validação de dados
##
### Pedir dois números inteiros e garantir que são válidos
##x = pede_int("Digite um número inteiro: ")
##y = pede_int("Digite outro número inteiro: ")
##
##De seguida, fora da função criada, vamos utilizar essa função associada às
##variáveis x e y em que pedimos ao utilizador a inserção dos dois números a
##calcular
##
##
###Validar divisão por zero
##while y == 0:
##print("Erro: O segundo número não pode ser zero para evitar divisão por zero.")
##y = pede_int("Digite outro número inteiro diferente de zero: ")
##
##Temos uma outra verificação e usamos o ciclo while para impedirmos que o
##segundo valor introduzido possa ser zero, uma vez que em matemática a
##divisão por zero não é possível.


## Slide 80
##O mesmo cálculo com validação de dados
##
##
### Cálculos
##soma = x + y
##subtra= x - y
##multip = x * y
##potencia = x ** y
##divisao = x/y
##
### Apresentar os resultados
##resultado = (
##)
##"Soma: {\nSubtração: {}\nMultiplicação: {}\nPotência: {}\nDivisão: {}".format( soma, subtra, multip, potencia, divisao) #\n serve para criar uma linha
##print("\nResultados: \n" + resultado)


##Podemos então criar as variáveis para os diferentes cálculos e guardar essa
##informação dentro de uma lista do tipo biblioteca com o nome resultado.
##E por fim temos a instrução print que apresenta os resultados obtidos, com
##base no input do utilizador.



## Slide 81
##E se quisermos que o utilizador possa voltar a
##calcular?
##
##Quando usamos bases de dados, muitas vezes precisamos de introduzir
##novos dados numa tabela. Podemos fazer isso através do python se
##permitirmos que no final o utilizador introduza novos dados, ou opte por sair do
##programa. Para fazermos isso no python precisamos de usar funções. Neste
##exemplo usamos duas: Uma para validar os números inteiros e outra para
##fazer os cálculos.
##
##
##def pede_int(mensagem):
##while True:
##try:
##numero= int(input(mensagem))
##return numero
##except ValueError:
##print("Erro: Por favor, digite um número inteiro válido.")
##
##Esta função para verificarmos se foi introduzido um número inteiro já tínhamos
##criado. Precisamos de seguida criar uma função para calcular, que vai ter tudo
##o que tínhamos anteriormente mais uma parte em que perguntamos se o
##utilizador quer repetir a introdução de dados.



## Slide 82
##Função calcular inclui variável repetir
##def calcular():
##    while True:
##        #Pedir dois números inteiros e garantir que são válidos
##        x = pede_int("Digite um número inteiro: ")
##        y = pedeint("Digite outro número inteiro: ")
##
##        #Validar divisão por zero
##        while y == O:
##            print("Erro: O segundo número não pode ser zero para evitar divisão por zero.")
##            y = pede_int("Digite outro número inteiro diferente de zero: ")
##
##        # Cálculos
##        soma = x + y
##        subtra = x - y
##        multip = x * y
##        potencia = x ** y
##        divisao = x / y
##
###Apresentar os resultados
##resultado = "Soma: MnSubtração: MnMultiplicação: MnPotência: MnDivisão: {}".format(
##    soma, subtra, multip, potencia, divisao))
##
##print("\nResultados: \n" + resultado)
##                                                                                        
###Perguntar se o utilizador quer repetir repetir
##repetir = input("\nQuer fazer novos cálculos? (S/N): ").strip().lower()
##if repetir != 's':
##    print("Encerra o programa.")
##    break 



## Slide 83
####Explicação do código
####Este código define a função calcular(), que realiza uma série de operações
####matemáticas entre dois números inteiros fornecidos pelo utilizador. O programa
####começa por pedir dois números inteiros através da função pede_int(), que
####garante que a entrada é válida. Em seguida, verifica se o segundo número é
####diferente de zero para evitar um erro de divisão por zero; se for zero, o utilizador
####precisa de introduzir um valor válido até que a condição seja cumprida.
####Depois de garantir que os valores são válidos, o programa calcula a soma,
####subtração, multiplicação, potência e divisão dos números e armazena os
####resultados na variável resultado, com cada operação apresentada numa linha
####separada. Após exibir o resultado, o programa pergunta ao utilizador se deseja
####realizar novos cálculos; se a resposta for diferente de "s", o programa encerra
####com uma mensagem de despedida.
####Contudo a função calcular apenas foi criada, ainda precisamos de a chamar
####através do código fora da função:
##
### Chamar a função para iniciar o programa
##calcular()



## Slide 84
##Exercício Registo de livros
##Exercício parte 1
##Cria um código com todas as variáveis
##necessárias para imprimir utilizando a função print
##(deve ser possível trocar nomes, preços e dados
##apenas alterando os valores das variáveis):
##Situação 01 - Gabriel é o cliente de uma livraria
##online que acaba de comprar 01 livro com o título
##lógica de programação por 19,30 €. O vendedor
##Marcos recebeu uma comissão de 3,50€ pela
##venda.
##
##
##Resultado esperado
##Print = ("Olá”, (Gabriel)
##sua compra de (01) qtd
##do livro por 19,30 € foi
##efetuada com
##sucesso!".
##"Olá, (Marcos) você
##acaba de receber uma
##comissão de3,50€ pela
##compra realizada
##pelo(a) cliente
##(Gabriel)".


## Slide 85
##Exercício Registo de livros
##exemplo de Solução

##Exemplo de solução:
##
###Variáveis
##client = "Manuel Sousa"
##vend = "Joana Afonso"
##livraria = "Burtana"
##titulo_livro = "Lógica de programação"
##preco_livro = 19.30
##comiss_vend = 3.50
##valor_comiss= preco_livro * (comiss_vend /100)
##
##print(f'" {client) foi à livraria {livraria}e comprou o livro {titulo_livro}por {preco_livro:.2f} €e o/a vendedor/a {vend} recebeu {comiss_vend} % de comissão""')
##print (f"{valor_comiss:.2f} € foi o valor que recebeu")
##
##
##
##Desafio maior:
##Cria um programa que pergunte estes dados ao utilizador, através do
##método input.



## Slide 86
##Exemplo de Solução
###variáveis com input do utilizador
##client =input("Qual o nome do cliente? ")
##vend = input("Qual o nome do/a vendedor? ")
##livraria = input("Qual o nome da livraria? ")
##titulo_livro = input("Qual o nome do livro comprado? ")
##preco_livro = float(input("Qual o preço do livro? "))
##comiss_vend = float(input("Qual a comissão do/a vendedor/a?"))
##valor_comiss= preco_livro * (comiss_vend /100)
##print(f"""{client} foi à livraria {livraria}
##e comprou o livro {titulo_livro}
##por {preco_livro:.2f} €
##e o/a vendedor/a {vend} recebeu {comiss_vend} % de comissão""")
##print (f" {valor_comiss:.2f} € foi o valor que recebeu")
##
##Desafio maior:
##Faz com que o programa tenha validação de dados


## Slide 87
##Exemplo de Solução
##Precisamos de criar duas
##funções usando o ciclo while
##true (enquanto for verdade).
##Uma função para os valores
##que verifica se são números
##e se são positivos e uma
##função para o texto que
##impeça de avançar se não for
##colocado texto algum, ou se
##colocar números.
##
##
##Desafio: Fazer com que o
##programa permita voltar a
##inserir os dados.



###Validação de dados
##
##
###Função para validar números
##def validar_numeros (mensagem):
##    while True:
##        try:
##            valor = float(input(mensagem))
##            if valor <0:
##            print("Erro: o valor não pode ser negativo.")
##            else:
##                return valor
##            except ValueError:
##                print("Erro: Por favor, insira um número válido.")
##
###Função para validar textos
##def validar_str (mensagem):
##    while True:
##        texto = input(mensagem).strip()
##        if texto.replace("", "").isalpha():
##            return texto
##        else:
##            print ("Erro o campo deve conter apenas letras e não estar vazio")
##
##
### Variáveis com input do utilizador e validação de dados
##client = validar_str("Qual o nome do cliente? ")
##vend = validar_str("Qual o nome do/a vendedor? ")
##livraria = validar_str("Qual o nome da livraria? ")
##titulo_livro = validar_str("Qual o nome do livro comprado? ")
##preco_livro = validar_numeros("Qual o preço do livro? ")
##comiss_vend = validar_numeros("Qual a comissão do/a vendedor/a?")
##
##
### Cálculo da comissão do vendedor
##valor_comiss = preco_livro * (comiss_vend / 100)
##
### Exibir as informações formatadas
##print("""{client} foi à livraria {livraria} e comprou o livro {titulo_livro}
##por {preco livro:.2f} € e o/a vendedor/a {vend}
##recebeu {comiss_vend} % de comissão""")
##
##print(f" {valor_comiss:.2f} € foi o valor que recebeu")
##


## Slide 88
##Solução para repetição
##
### Função para validar números
##def validar_numeros(mensagem):
##    while True:
##        try:
##            valor = float(input(mensagem))
##            if valor < 0:
##            print("Erro: o valor não pode ser negativo.")
##            else:
##                return valor
##            except ValueError:print("Erro: Por favor, insira um número válido.")
##
### Função para validar textos
##def validar_str(mensagem):
##    while True:
##        texto = input(mensagem).strip()
##        if texto.replace("", "").isalpha():
##            return texto
##        else:print("Erro: o campo deve conter apenas letras e não estar vazio")
##        
##Começamos por criar
##as duas funções de
##validação de números
##e de texto
##
##Aqui precisamos de uma função para validar números e outra para validar
##strings e uma outra que vai pegar nas duas anteriores para apresentar os
##dados e perguntar se quer inserir de novo.



## Slide 89
##Criamos então a
##função principal que
##vai integrar as funções
##anteriores, fazer os
##cálculos necessários e
##perguntar se quer
##repetir.
##
##Solução para repetição
### Função principal para introdução e cálculo de dados
##def processo_compra():
##    while True:
### Variáveis com input do utilizador e validação de dados
##client = validar_str("Qual o nome do cliente?")
##vend = validar_str("Qual o nome do/a vendedor/a?")
##livraria = validar_str("Qual o nome da livraria? ")
##titulo_livro = validar_str("Qual o nome do livro comprado? ")
##preco livro = validar_numeros("Qual o preço do livro?")
##comiss_vend = validar_numeros("Qual a comissão do/a vendedor/a?")
##
### Cálculo da comissão do vendedor
##valor_comiss = preco_livro * (comiss_vend / 100)
##
### Exibir as informações formatadas
##print("""{client} foi à livraria {livraria} e comprou o livro {titulo_livro}
##por {preco_livro:.2f} € e o/a vendedor/a {vend}
##recebeu {comiss_vend}% de comissão, o que equivale a {valor_comiss:.2f} €.""")
##
### Perguntar se o utilizador deseja fazer outra introdução de dados
##repetir = input("\nDeseja fazer outra compra? (S/N): ").strip().lower()
##if repetir != 's':
##    print("Encerra o programa.")
##    break
##
##Por fim precisamos de chamar a função relativa ao processo de compra, pois
##a função foi criada mas ainda não foi utilizada.
##
### Executar o programa
##processo_compra()



## Slide 90
##Exercício para praticar Cálculos com repetição
##Desafio:
##Crie um programa que
##permita validação de
##dados para este exemplo

###Criamos uma função com o que pretendemos
##def calcular():
##
##num1 = int(input("Digite o primeiro número?"))
##num2 =int(input("Digite o segundo número? "))
##
###realizar cálculos
##soma = num1+num2
##subt = num1-num2
##mult = num1*num2
##potencia = num1**num2
##div = num1/num2
##
###Criar lista de resultados
##
##resultados =[
##
##"A soma dos 2 numeros é: {}".format(soma),
##"A subtração do primeiro número pelo segundo é: {}".format(subt),
##"O resultado da multiplicação é: {}".format(mult),
##"A potência do primeiro número elevado ao segundo é: {}".format(potencia),
##"A divisão do primeiro número pelo segundo é: {}".format(div)
##
##]
##
###Apresentar os resultados usando o ciclo for
##for n in (resultados):
##    print (n)
##
###loop para usar a função calcular e permitir calcular outra vez
##while True:
##    calcular()
##    print()
##    repetir = input ("Quer calcular outra vez? (S/N)").strip().upper()
##    print()
##    if repetir != "S":
##        print ("Obrigado, não vão ser realizados os cálculos de novo")
##        break


## Slide 91
##Solução; primeiro criamos a função calcular() com
##validação de dados
##
##
##Na primeira parte do
##código criamos uma
##função e dentro dela as
##condições para verificar se
##os dados introduzidos pelo
##utilizador são válidos.


##
### Criamos uma função com o que pretendemos
##def calcular():
##while True:
##        try:
##num1 = int(input("Digite o primeiro número: "))
##break
##except ValueError:print("Erro: Por favor, insira um número inteiro válido.")
##while True:
##    try:
##num2 = int(input("Digite o segundo número: "))
##if num2 == 0:
##
##print("Erro: O segundo número não pode ser zero para evitar divisão por zero.")
##continue
##break
##
##except ValueError:print("Erro: Por favor, insira um número inteiro válido.")
##
### Realizar cálculos
##soma = num1 + num2
##subt = num1 - num2
##mult = num1 * num2
##potencia = num1 ** num2
##div = num1 / num2
##
### Criar lista de resultados
##resultados = ["A soma dos 2 números é: {}".format(soma),
##              "A subtração do primeiro número pelo segundo é: {}".format(subt),
##              "O resultado da multiplicação é: {}".format(mult),
##              "A potência do primeiro número elevado ao segundo é: {}".format(potencia),
##              "A divisão do primeiro número pelo segundo é: {:.2f}".format(div)
##              ]
##
### Apresentar os resultados usando o ciclo for
##for n in resultados:
##    print(n)
##


## Slide 92
##Depois fora da função calcular vamos criar o ciclo que nos
##permite chamar a função e repetir até que o utilizador deseje
##parar o programa
##
##
###Loop para usar a função calcular e permitir calcular outra vez
##while True:
##    calcular()
##    print()
##    repetir = input("Quer calcular outra vez? (S/N): ").strip().upper()
##    print()
##    if repetir != "S":
##        print("Obrigado, não vão ser realizados os cálculos de novo.")
##        break
##
##Enquanto for verdade vai ser repetida a função calcular() que no final de
##cada execução pergunta se queremos calcular de novo. Se o utilizador
##responder com s (em letra pequena ou em maiúsculas). caso dê qualquer
##outra resposta o programa apresenta uma mensagem e pára (break)



## Slide 93
##Exercício Calculadora simples
##
### Calculadora simples de soma
##numero1 = float(input("Digite o primeiro número: "))
##numero2 = float(input("Digite o segundo número: "))
##
##soma = numero1 + numero2 # Soma dos números
##print("A soma dos números é:", soma)
##
##
##
##Desafios:
##Pede ao utilizador para inserir dois números. Calcula e mostra: A soma,
##a diferença do primeiro para o segundo número, a média, a
##multiplicação e a divisão.
##Altera o programa para ter validação de dados e a possibilidade de
##repetição



## Slide 94
##Exercício métodos print() e input()
### Exemplo: Uso de variáveis e métodos print e input
##"""Objetivo:Introduzir variáveis, a função print para exibir mensagens,
##e input para receber dados do utilizador."""
##
##nome = input("Qual é o teu nome? ") # Recebe o nome do utilizador
##idade = int(input("Qual é a tua idade? ")) # Recebe a idade e converte para inteiro
##
##print("Olá,", nome, "!") # Exibe uma mensagem de boas-vindas
##print("Em 10 anos, terás", idade + 10, "anos.") # Calcula a idade daqui a 10 anos e exibe
##
##Desafio:
##Cria um script que pergunte ao utilizador o nome, a cidade onde vive e
##o seu hobby favorito, armazene estas informações em variáveis e exiba
##uma mensagem personalizada, como: "Olá, [nome]! Vejo que gostas de
##[hobby] e vives em [cidade]!"


## Slide 95
### Exemplo com len()` para medir o comprimento de uma string
##nome = input("Qual é o teu nome? ")
##comprimento = len(nome) # Calcula o número de caracteres no nome
##print("O teu nome tem", comprimento, "caracteres.")
##
##Exercício método len()
##
##
##Desafio:
##Pede ao utilizador para inserir o nome completo e exibe quantos
##caracteres o nome completo tem (incluindo espaços).



## Slide 96
##Exercício métodos upper() e lower()
##
### Exemplo com upper() e lower() para manipulação de maiúsculas e minúsculas
##cidade = input("Qual é a tua cidade? ")
##print("Cidade em maiúsculas:", cidade.upper()) # Converte a cidade para maiúsculas
##print("Cidade em minúsculas:", cidade. lower()) # Converte a cidade para minúsculas
##
##Desafio:
##Pede ao utilizador para inserir uma frase. Exibe a frase em:
##Maiúsculas;
##Minúsculas;
##E o comprimento da frase.


## Slide 97
##Exercício método type()
### Exemplo com o métodp type() para verificar tipos de dados:
##numero= int(input("Digite um número: "))
##print("O tipo da variável numero antes da conversão é:", type(numero))
##
##numero = str(numero) # Converte o número inteiro para string
##print("O tipo da variável numero após a conversão é:", type(numero))
##
##
##Desafio:
##Pede ao utilizador para inserir qualquer valor. Exibe:
##O valor digitado;
##O tipo de dados original do valor;
##Converte o valor para string e exibe o novo tipo de dados.
##



## Slide 98
##Exercício Conversão de Tipos com int(),
##float(), str()
##
##
### Exemplo com conversão de tipos
##numero1 = int(input("Digite um número inteiro: ")) # Converte para inteiro
##numero2 = float(input("Digite um número decimal: ")) # Converte para decimal
##
### Converte os resultados para string e exibe uma frase
##print("O número inteiro é " + str(numero1) + " e o número decimal é " + str(numero2) + ".")
##
##
##
##Desafio:
##Pede ao utilizador um valor decimal e um valor inteiro. Calcula e exibe:
##A soma dos dois valores, exibindo o resultado como um número
##decimal;
##Uma frase que mostre ambos os números numa frase (por exemplo, "O
##número inteiro é X e o decimal é Y").



## Slide 99
##Exercício Validação de dados
##
### Exemplo de validação de input para um número inteiro
##while True:
##entrada = input("Por favor, insira um número inteiro: ")
##if entrada.isdigit(): # Verifica se a entrada é um número inteiro
##    numero_inteiro = int(entrada) # Converte para inteiro
##    print("Obrigado! O número inteiro inserido foi:", numero_inteiro)
##    break
##else:
##    print("Erro: Por favor, insira um número inteiro válido.")
##
##
##
##Desafio:
##Crie um programa que peça ao utilizador para inserir um número inteiro,
##multiplique o número por 2 e exiba o resultado. Se o utilizador inserir
##algo que não seja um número inteiro, exiba uma mensagem de erro e
##permita tentar novamente.



## Slide 100
##Outro exercício com validação
##
### Exemplo de validação de input para um número decimal
##while True:
##    entrada = input("Por favor, insira um número decimal: ")
##    try:
##    numero_decimal = float(entrada) # Tenta converter para float
##    print("Obrigado! O número decimal inserido foi:", numero_decimal)
##    break
##except ValueError:
##    print("Erro: Por favor, insira um número decimal válido.")
##
##Desafio:
##Escreva um programa que peça ao utilizador para inserir um número
##inteiro, calcule o quadrado desse número e exiba o resultado.
##Se o utilizador inserir um valor inválido, exiba uma mensagem de erro e
##permita tentar novamente.



## Slide 101
##Exercício controle tipo de dados inseridos
##Par ou ímpar
##
### Exemplo de validação de input para um número inteiro num intervalo específico
##while True:
##    entrada = input("Insira um número inteiro entre 1 e 10: ")
##    if entrada.isdigit():
##        numero_inteiro = int(entrada)
##        if 1 <= numero_inteiro <= 10: # Verifica se está no intervalo desejado
##        print("Obrigado! O número está dentro do intervalo:", numero_inteiro)
##        break
##    else:
##    print("Erro: O número deve estar entre 1 e 10.")
##    else:
##    print("Erro: Por favor, insira um número inteiro válido.")
##
##
##Desafio:
##Desenvolva um programa que peça ao utilizador para inserir um número
##inteiro entre 1 e 100 para verificar se é par ou ímpar
##Se o número estiver dentro do intervalo, diga ao utilizador se o número é
##par ou ímpar. Se o input estiver fora do intervalo ou não for um número
##inteiro, exiba uma mensagem de erro e permita uma nova tentativa.



## Slide 102
##Exercício controle tipo de dados inseridos
##Par ou impar (uma Solução possível)
##
##while True:
##    entrada = input("Insira um número inteiro entre 1 e 100 para verificar se é par ou ímpar: ")
##    if entrada.isdigit():
##    numero_inteiro = int(entrada)
##    if 1 <= numero_inteiro <= 100:
##        if numero_inteiro % 2 == 0:
##            print("O número inserido é par.")
##            else:
##            print("O número inserido é ímpar.")
##            break
##            else:
##            print("Erro: O número deve estar entre 1 e 100.")
##            else:
##            print("Erro: Por favor, insira um número inteiro válido.")




## Slide 103
##Exercício controle tipo de dados inseridos
##Apenas strings
##
### Exemplo de validação de input para uma palavra
##while True:
##entrada = input("Por favor, insira uma palavra (apenas letras): ")
##if entrada.isalpha():
##    # Verifica se a entrada contém apenas letras
##    print("Obrigado! A palavra inserida foi:", entrada)
##    break
##else:
##    print("Erro: Por favor, insira apenas letras, sem números ou caracteres especiais.")
##
##Desafio:
##Crie um programa que peça ao utilizador para inserir uma palavra que
##contenha apenas letras.
##Conte e exiba quantas vogais há na palavra.Se o input contiver números
##ou caracteres especiais, exiba uma mensagem de erro e permite nova
##tentativa.



## Slide 104
##Exercício controle tipo de dados inseridos
##Apenas strings solução do desafio
##
##
##while True:
##entrada = input("Insira uma palavra (apenas letras) para contar as vogais: ")
##
##if entrada.isalpha():
##    vogais = "aeiouAEIOU"
##    contagem_vogais = 0
##    for letra in entrada:
##    if letra in vogais:
##        contagem_vogais += 1 # Soma 1 para cada vogal encontrada
##        print("A palavra inserida contém", contagem_vogais, "vogais.")
##        break
##    else:
##        print("Erro: Por favor, insira apenas letras, sem números ou caracteres especiais.")


#### Slide 105
##Exercício controle tipo de dados inseridos
##Apenas strings solução do desafio
##
##Uma outra forma seria:
##
##
##while True:
##entrada = input("Insira uma palavra (apenas letras) para contar as vogais: ")
##if entrada.isalpha():
##vogais = "aeiouAEIOU"
##contagem_vogais = sum(1 for letra in entrada if letra in vogais)
##print("A palavra inserida contém", contagem_vogais, "vogais.")
##break
##else:
##print("Erro: Por favor, insira apenas letras, sem números ou caracteres especiais.")
##



## Slide 106 
##Exercício condições
##Estrutura básica com if e else
##
### Exemplo básico de condição if e else
##numero = int(input("Insira um número: "))
##
##
##if numero > 0:
##print("O número é positivo.")
##else:
##print("O número é zero ou negativo.")
##
##Desafio:
##Crie um programa que peça ao utilizador para inserir um número inteiro.
##Verifique se o número é positivo, negativo ou zero. Se o utilizador inserir
##um valor que não é um número, exiba uma mensagem de erro e peça
##que tente novamente.



## Slide 107
##Exercício condições
##Estrutura básica com if e else solução
##
### Exemplo básico de condição if e else com validação de entrada
##while True:
##entrada = input("Insira um número: ")
##if entrada.Istrip('-').isdigit(): # Permite números negativos e verifica se é um número inteiro numero= int(entrada)
##if numero > 0:
##print("O número é positivo.")
##else:
##print("O número é zero ou negativo.")
##break
##else:
##print("Erro: Por favor, insira um número inteiro válido.")
##
##Desafio maior:
##Crie um programa que permita dizer qual é o número digitado e que
##admita números do tipo float.



## Slide 108 
##Exercício condições
##Estrutura básica com if, else e elif Solução
### Exemplo com validação para números float e int
##while True:
##entrada = input("Insira um número: ")
##try:
##numero= float(entrada) # Tenta converter a entrada para float
##if numero > 0:
##print(f"O número {numero} é positivo.")
##elif numero < 0:
##print(f"O número {numero} é negativo.")
##else:
##print("O número é zero.")
##break # Sai do loop após entrada válida except ValueError:
##print("Erro: Por favor, insira um número válido (inteiro ou decimal).")



## Slide 109
##Exercício condições
##Estrutura básica com if, else e elif Solução
##Explicação do Código:
##Para aceitar números do tipo float, precisamos de usar um bloco try...except
##que verifica se a entrada é um número decimal (float) ou inteiro. Se o
##utilizador inserir algo inválido (como texto), o programa exibirá uma
##mensagem de erro e pedirá que tente novamente.
##Condições if, elif, else: Após garantir que o valor é numérico, o código
##verifica: Se o número é maior que zero, se é menor que zero, ou se é
##exatamente zero.
##f-strings: Utilizamos f"{numero}" para incluir o valor digitado diretamente na
##mensagem que é apresentada.



## Slide 110
##Exercício com restrição de valores a inserir e usando
##o ciclo for
##Temos uma função com 3
##parâmetros que nos vai
##permitir controlar a
##mensagem, o valor
##mínimo aceitável e o
##valor máximo e de
##seguida usamos o ciclo
##for para mostrar os
##valores do menor para o
##maior.
##
##"""programa em que se pergunta qual o valor inicial (entre -10 e 10 e final (entre 11 e 20)
##e depois aplica-se o ciclo for"""
##def pedir_valor(mensagem, minimo, maximo): while True:
##try:
##valor = int(input(mensagem))
##if minimo <= valor <= maximo:
##return valor
##else:
##print("Erro: Insira um valor entre {minimo} e {maximo}.")
##except ValueError:
##print("Erro: Por favor, insira um número inteiro válido.")
### Pedir o valor inicial (entre -10 e 10)
##valor_inicial = pedir_valor("Digite o valor inicial (entre -10 e 10): ", -10, 10)
### Pedir o valor final (entre 11 e 20)
##valor_final = pedir_valor("Digite o valor final (entre 11 e 20): ", 11, 20)
### Ciclo for para imprimir os números no intervalo
##for n in range(valor_inicial, valor_final + 1):
##print(n)



## Slide 111
##Exercício ciclo while True e for com validação de
##dados
##Aqui temos uma situação em
##que uma função chama outra
##função e no final temos a
##possibilidade de inserir novos
##dados.
##A função a ser chamada
##pedir_valor(mensagem,
##minimo, maximo) precisa de
##ser colocada acima da função
##ciclo_valores() pois esta
##depende da anterior.
##Neste caso a função
##pedir_valor tem 3 parâmetros.
##
##"""programa em que se pergunta qual o valor inicial
##(entre -10 e 10 e final (entre 11 e 20)
##e depois aplica-se o ciclo for e no final pergunta se queremos repetir"""
##def pedir_valor(mensagem, minimo, maximo):
##while True:
##try:
##valor = int(input(mensagem))
##if minimo <= valor <= maximo:
##    return valor
##else:
##print(f"Erro: Insira um valor entre {minimo} e {maximo}.")
##except ValueError:
##print("Erro: Por favor, insira um número inteiro válido.")
##
##
##def ciclo_valores():
### Pedir o valor inicial (entre -10 e 10)
##valor_inicial = pedir_valor("Digite o valor inicial (entre -10 e 10): ", -10, 10)
### Pedir o valor final (entre 11 e 20)
##valor_final = pedir_valor("Digite o valor final (entre 11 e 20): ", 11, 20)
### Ciclo for para imprimir os números no intervalo print("Números no intervalo:")
##for i in range(valor_inicial, valor_final + 1):
##print(i)
##
##
##while True:
##ciclo_valores()
##
##
### Perguntar se o utilizador quer repetir
##repetir = input("Quer repetir e inserir novos valores? (S/N): ").strip().upper()
##if repetir != 'S':
##print("Programa finalizado.")
##break



## Slide 112
##Exercício de exemplo desenhar na tela criada
##
##Aqui usamos a biblioteca
##externa ou classe Turtle e
##a partir dela os métodos
##que fazem parte dessa
##classe que nos permitem
##criar a janela e desenhar.
##
##
##
##""" Criar um desenho
##de vários circulos
##num fundo preto"""
##
##import turtle
##
##
### Configuração inicial
##tela = turtle.Screen()
##tela.bgcolor("black") # Definir fundo preto
##
##
### Criar caneta para desenhar
##caneta = turtle.Turtle()
##caneta.hideturtle() # Esconde a caneta
##caneta.speed(100) # gerir a velocidade do desenho
##
##
### Lista de cores para os círculos
##cores = ["red", "yellow", "blue", "green", "purple"]
##
##
### Desenhar círculos com diferentes raios
##raios = [50, 100, 150, 200, 250]
##
##
### Loop para desenhar os círculos
##for i in range(len(raios)):
##caneta.penup() # Levanta a caneta para não desenhar enquanto se move
##caneta.goto(0, -raios[i]) # Posiciona a paneta no local correto
##caneta.pendown() # Ativaa caneta para desenhar
##caneta.color(cores[i % len(cores)]) # Define a cor do círculo
##caneta.circle(raios[i]) # Desenha o círculo com o raio atual
##
##
### Manter a tela aberta
##turtle.done()



## Slide 113
##Exercício de exemplo Jogo do Galo
##
##Aqui usamos a biblioteca
##THINKER e a partir dela
##os métodos que fazem
##parte dessa classe que
##nos permitem criar a
##aplicação



## Slide 114
##Exercício de exemplo Jogo do Galo
##Receita parte 1
##Importamos a classe Thinker e a sub classe messagebox.
##Criamos a janela da aplicação


##import tkinter as tk # Importa o módulo tkinter
##from tkinter import messagebox # Para apresentar mensagens
##
### Configurações gerais da janela
##
##janela = tk.Tk() #Cria a janela principal da aplicação tkinter
##
##janela.title("JOGO DO GALO VERSÃO 1.0") # Titulo da janela
##janela.geometry("600x600") # Altura e largura da janela
##janela.resizable (False, False) # janela da app não pode ser redimensionada
##janela.configure(bg='darkblue') # Cor da janela
##janela.wm_attributes('-alpha', 0.7) # Janela semi-transparente



## Slide 115
##Receita parte 2
##Criamos o tabuleiro 3x3
##Criamos o título e os botões
##
##
### Variáveis do jogo
##jogador_atual = "X"
##
### Cria uma matriz 3x3 vazia para representar o tabuleiro do jogo
##tabuleiro = [["" for _ in range(3)] for in range(3)]
##
##
### Criar o título
##
##titulo = tk.Label(janela, text="Jogo do Galo", font=("Verdana", 14, "bold"), bg='darkblue', fg='white')
##titulo.pack(pady=20)
##
### Frame para o tabuleiro, para que fique centrado e opaco
##frame_tabuleiro = tk. Frame(janela, bg='white')
##frame_tabuleiro. pack (pady=40)
##
### Criar os botões do tabuleiro
##"""
##cria uma interface gráfica com botões organizados
##
##numa grelha 3x3 usando a biblioteca Tkinter em Python.
##
##A lista botoes é criada inicialmente como uma lista vazia. Esta lista é uma matriz com 3 linhas e 3 colunas.
##
##Os botões são colocados dentro de cada célula.
##"""
##
##botoes = []
##
##for i in range(3):
##    linha = []
##for j in range(3):
##
##botao = tk.Button(frame_tabuleiro, text="", font=("Arial", 20), width=5, height=2,
##
##command lambda x=i, y=j: clique(x, y))
##
##botao.grid(row=i, column=j)
##
##linha.append(botao)
##
##botoes.append(linha)



## Slide 116
##Receita parte 3
##Criamos a função para verificar se alguém venceu
##
##
### Função para verificar vitória
##def verifica_vitoria():
##for i in range(3):
##
##"""Verificar linhas e colunas
##
##Verificar se todos os elementos
##
##de uma linha no tabuleiro são iguais e não estão vazios."""
##
##if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
##
##return tabuleiro[i][0] #Retorna o valor do primeiro elemento da linha i do tabuleiro.
##
###Verificar se uma linha ou coluna é igual e não vazia; se sim, retorna o valor.
##
##if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
##    return tabuleiro[0][i]
##
### Verifica diagonais
##
##if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "";
##    return tabuleiro[0][0]
##
##if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
##    return tabuleiro[0][2]
##    return None



## Slide 117
##Receita parte 4
##Criamos a função para verificar se há empate
##
##
### Função para verificar empate
##
##"""Verificar se há células vazias no tabuleiro. Se não houver, retorna True indicando empate.
##"""
##
##def verifica_empate():
##
##for linha in tabuleiro:
##
##if "" in linha:
##    return False
##return True



## Slide 118
##Receita parte 5
##Criamos a função para verificar a interação com os botões
##
##
### Função para detetar e responder ao clique nos botões
##def clique(x, y):
##global jogador_atual
##if tabuleiro[x][y] == "": # Verifica se a célula está vazia
##tabuleiro[x][y]= jogador_atual
##botoes[x][y]["text"] = jogador_atual #Vai colocar X ou 0 em função da vez de jogar
##vencedor = verifica_vitoria() #Chama a função verificar vitória
##if vencedor:
##messagebox.showinfo("Fim de Jogo", f"O jogador {vencedor} venceu!")
##janela.quit()
##elif verifica_empate():
##messagebox.showinfo("Fim de Jogo", "Empate!")
##janela.quit()
##else:
##jogador_atual = "O" if jogador_atual == "X" else "X" # Muda de jogador e continua
##
##Receita parte 6
##Instrução para correr a aplicação
##
###Instrução para fazer correr o jogo
##janela.mainloop()

############ PARTE 1 ACABOU


## Slide 2
##Criar servidor local com base de dados mysql através do XAMPP



## Slide 3
##Instalação do pacote XAMMP
##Existem outros pacotes que integram Apache, php e mysql como o
##Wampserver, mas neste caso vamos usar o XAMMP que funciona bem
##para fins académicos e de aprendizagem*.
##
##
##Não é obrigatório instalar esta pacote se já tiverem outro que
##tenha as mesmas funcionalidades.



## Slide 4
##Link para download e instalação:
##https://www.apachefriends.org/download.html
##
##



## Slide 5
##Depois de fazermos o download da aplicação, para instalar o XAMMP
##seguimos todos os passos e clicamos em Next. Se aparecer esta
##mensagem de aviso, devemos ter em atenção que não podemos instalar
##no caminho original, devemos escolher outro local.
##
##
##Isso pode acontecer porque já temos um servidor local



## Slide 6
##Aqui podemos escolher todos os componentes, mesmo que apenas
##sejam usados mais adiante.




## Slide 7
##Aqui pode ser necessário escolher outra pasta. Neste caso vou criar
##uma pasta testes dentro do caminho sugerido, para contornar algum
##conflito que possa existir.
##
##
##Select a folder C:\xampp



## Slide 12
##Quando abrimos o XAMPP entramos no painel de controle aqui é que
##ativamos os serviços que precisamos. Por agora escolhemos ativar
##Apache e mySQL Para isso clicamos em Start para cada um e esperamos
##que fique verde. Se aparecere uma mensagem de permissão escolhemos
##sim.



## Slide 13
##Depois de instalarmos o Apache e o MySQL, precisamos de entrar na
##página de admin da base de dados do MYSQL,



## Slide 14
##Depois de clicarmos abre-se uma página web de admin do mySQL dentro
##do localhost.



## Slide 15
##Por agora não vamos criar nenhuma base de dados, mas para o fazermos
##precisamos de ir ao separador Bases de dados



## Slide 17
##Ligar Base de Dados MySQL com o Python
##
##Precisamos de ligar o Python ao MySQL:
##    
##Na linha de comandos do windows ou do Linux, ou no terminal
##do Mac adicionamos a instrução:
##pip install mysql-connector-python



## Slide 18
##Ligar Base de Dados MySQL com o Python
##Precisamos de ter o sistema Apache e MySQL ativos:
##No XAMMP clicamos em ativar para ambos e depois clicamos
##no Admin do MySQL



## Slide 19
##Ligar Base de Dados MySQL com o Python
##Precisamos de ter uma base de dados criada:
##No exemplo já temos uma chamada clientes. Mas se não
##tiverem basta clicar em Base de Dados e criar



## Slide 20
##Ligar Base de Dados MySQL com o Python
##
##import mysql.connector
##
##conectar = mysql.connector.connect(host='localhost',
##                                   database ='clientes',
##                                   user='root', password='')
##if conectar.is_connected():
##
##db_info = conectar.get_server_info()
##
##print ("Conexão realizada com sucesso ao servidor versão", db_info)
##
##cursor conectar.cursor()
##
##cursor.execute("select database();")
##
##linha = cursor.fetchone()
##
##print ("Ligado à base de dados: ", linha)
##
##Agora precisamos de criar um script para ver se está tudo a
##funcionar:
##No exemplo usamos a base de dados clientes, o user é o pré definido na
##instalação do XAMMP e ainda não tem password. Por agora só estamos
##a testar se a ligação está a acontecer. No futuro, se não estivermos a
##usar o mySQL apenas para fins de aprendizagem, é conveniente termos
##uma password.



## Slide 21
##Ligar Base de Dados MySQL com o Python
##Gravamos e fazemos correr:
##Se tudo correr como o previsto iremos ter as seguintes
##mensagens


##===== RESTART: C:/Users/dio_m/OneDrive/Desktop/exerciciosP/ligarpto mysql.py ====
##
##Conexão realizada com sucesso ao servidor versão 5.5.5-10.4.32-MariaDB
##Ligado à base de dados: ('clientes',)




## Slide 23
##Criar tabelas no mysql com o Python
##
##É algo que não é comum fazer-se mas pode ser útil em algumas situações.
##
##
##Para tudo funcionar é importante termos o localhost e a ligação ao mySQL
##ativa.
##
##No caso de termos um site online, por exemplo através do wordpress,
##precisamos de ter os acessos e o mySQL ativo no wordpress.
##
##Criar tabelas no mysql com o Python
##Para configurar o acesso a páginas reservadas, é necessário um plugin de
##membership ou de gestão de acessos.
##
##
##Algumas opções populares são: MemberPress: Gera páginas reservadas,
##controla registos e permite personalizar os níveis de acess;
##
##Paid Memberships
##Pro: Permite configurar diferentes níveis de acesso e é uma opção robusta com
##funcionalidades premium;
##
##Restrict Content Pro: Este plugin permite restringir o
##conteúdo a utilizadores registados e oferece opções de personalização.



## Slide 24
##Para fins académicos vamos usar o localhost com o Apache ativo,
##base de dados mySQL ativa e o python com mysql-connector ativo
##
##
##Entramos no admin do MySQL e criamos uma base de dados, para
##criarmos dentro dela uma tabela através do python.



## Slide 25
##A base de dados que vamos criar deve ter um nome relacionado com o
##que pretendemos fazer. Imaginemos que temos uma loja de roupa e
##acessórios de moda com o nome Tstore.
##
##
##Vamos dar esse nome à base de dados
##
##Repara que depois de
##clicarmos em criar,
##nenhuma tabela foi criada.
##Vamos fazer isso através
##do Python.




## Slide 26
###Criar o script de criação de tabela no python
##Neste exemplo vamos criar a tabela de
##produtos, com o nome produtos.
##
##Para isso criamos um novo script em python
##com o nome CriarTabela e inserimos o
##seguinte código:
##    
##Criar o script de criação de tabela no python
##Começamos por importar o mysql,conenctor, através da instrução:
##import mysql.connector
##
##De seguida criamos uma função para
##criar a tabela de produtos, através da instrução:
##def criar_tabela():






## Slide 26
###Script da tabela Python Tstore - 1
##import mysql.connector
##
### Função para criar o banco de dados se não existir
##def criar_base_dados():
##    try:
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password=""
##        )
##        mycursor = mydb.cursor()
##        mycursor.execute("CREATE DATABASE IF NOT EXISTS tstore")
##        print("Base de dados 'tstore' criada com sucesso!")
##    except mysql.connector.Error as err:
##        print(f"Erro ao criar a base de dados: {err}")
##    finally:
##        if 'mycursor' in locals() and mycursor:
##            mycursor.close()
##        if 'mydb' in locals() and mydb.is_connected():
##            mydb.close()
##
### Função para criar a tabela de produtos
##def criar_tabela():
##    try:
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )
##
##        if mydb.is_connected():
##            print("Conexão com a base de dados realizada com sucesso!")
##
##            mycursor = mydb.cursor()
##
##            # Criar tabela Produtos se não existir
##            mycursor.execute("""
##                CREATE TABLE IF NOT EXISTS Produtos (
##                    Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
##                    Produto_nome VARCHAR(255),
##                    Produto_foto LONGBLOB,
##                    Produto_price FLOAT,
##                    Produto_Quantidade INT
##                )
##            """)
##
##            print("Tabela 'Produtos' criada com sucesso ou já existe.")
##
##    except mysql.connector.Error as err:
##        print(f"Erro ao criar a tabela: {err}")
##
##    finally:
##        if 'mycursor' in locals() and mycursor:
##            mycursor.close()
##        if 'mydb' in locals() and mydb.is_connected():
##            mydb.close()
##
### Executar as funções
##criar_base_dados()  # Primeiro cria a base de dados
##criar_tabela()      # Depois cria a tabela
##
##



##Base de dados 'tstore' criada com sucesso!
##Conexão com a base de dados realizada com sucesso!
##Tabela 'Produtos' criada com sucesso ou já existe.




## Slide 27
##Explicação do código passo a passo
##
##import mysql.connector
##
##
### Função para criar a tabela de produtos
##def criar_tabela():
##try:
### Conectar ao banco de dados
##mydb = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="",
##    database="tstore"
##)
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print("Conexão com a base de dados realizada com sucesso!")
##
##Começamos por importar a biblioteca mysql.connector. Depois
##criamos a função que vai conectar o Python ao mySQL e verificamos
##se a ligação foi bem sucedida.



## Slide 28
##De seguida, ainda dentro desta função, vamos criar um cursor que vai
##escrever no SQL as instruções para criar a tabela.


##mycursor = mydb.cursor()
##
### Criar tabela Produtos se não existir
##    mycursor.execute("""
##CREATE TABLE IF NOT EXISTS Produtos (
##
##Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
##Produto_nome VARCHAR(100),
##Produto_descrit VARCHAR(500),
##Produto_price FLOAT,
##Produto_Quantidade INT
##)
##""")



## Slide 29
##Ainda dentro da função, precisamos então de confirmar
##se a tabela foi criada e, fazer uma validação
##para o caso de não ser e desconectamos o
##cursor e a ligação do python à base de dados.
##
##
### Confirmar que a tabela foi criada
##print("Tabela Produtos criada com sucesso ou já existe.")
##
##except mysql.connector.Error as erro:
##    print(f"Erro ao criar a tabela: {erro}")
##finally:
##if mydb.is_connected():
##    mycursor.close()
##    mydb.close()
##
##
##E por fim, fora da função que criámos, executamos a função criar_tabela()
##
### Utilizar a função criar_tabela
##criar_tabela()






## Slide 30
##O código completo:
##
##import mysql.connector
##
### Função para criar a tabela de produtos
##def criar_tabela():
##try:
### Conectar ao banco de dados
##mydb = mysql.connector.connect(
##host="localhost",
##user="root",
##password="",
##database="tstore"
##)
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print("Conexão com a base de dados realizada com sucesso!")
##
##mycursor = mydb.cursor()
##
##
### Criar tabela Produtos se não existir
##mycursor.execute("""
##
##CREATE TABLE IF NOT EXISTS Produtos (
##Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
##Produto_nome VARCHAR(255),
##Produto_foto LONGBLOB,
##Produto_price FLOAT,
##Produto Quantidade INT
##)
##""")
##
##
### Confirmar que a tabela foi criada
##
##print("Tabela Produtos criada com sucesso ou já existe.")
##
##except mysql.connector.Error as err:
##    print("Erro ao criar a tabela: {err}")
##finally:
##
##if  mydb.is_connected():
##    mycursor.close()
##    mydb.close()
##
### Utilizar a função criar_tabela
##criar_tabela()




## Slide 31
##Desafio: Criar tabela de clientes
##Pretendemos agora criar uma nova tabela de clientes dentro da mesma
##base de dados. O código será muito semelhante, o que muda é o nome
##da tabela e os campos que irão fazer parte da mesma.
##Neste caso queremos ter uma chave primária cliente_id e os campos
##Nome, Apelido, Email, Telefone, Morada, codigo_postal, Localidade e
##País
##Antes de veres como se faz, tenta fazer, usando como base o que já
##foi feito anteriormente com a tabela produtos.



##Slide 32
##Como se faz
##Importamos o mysql.connector, criamos a função criar tabela de clientes
##(criar_tabela_cleintes()) e dentro dela começamos por verificar se a
##conexão foi estabelecida e criamos um cursor para podermos interagir
##com o SQL.



##import mysql.connector
##
### Função para criar a tabela de clientes
##def criar_tabela_clientes():
##    try:
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )
##
##        if mydb.is_connected():
##            print("Conexão com a base de dados realizada com sucesso!")
##
##            mycursor = mydb.cursor()



##Slide 33
#### Ainda dentro dessa função pedimos ao cursor para executar os
####comandos SQL que vão gerar a tabela.
##            
##            # Criar tabela Clientes se não existir
##            mycursor.execute("""
##                CREATE TABLE IF NOT EXISTS Clientes (
##                    Cliente_Id INT AUTO_INCREMENT PRIMARY KEY,
##                    Nome VARCHAR(100),
##                    Apelido VARCHAR(100),
##                    Email VARCHAR(100) UNIQUE,
##                    Telefone VARCHAR(20),
##                    Morada VARCHAR(255),
##                    Codigo_postal VARCHAR(10),
##                    Localidade VARCHAR(100),
##                    País VARCHAR(50)
##                )
##            """)



##Slide 34
####Ainda dentro desta função vamos confirmar se a tabela foi criada e se
####não vamos verificar se existe algum erro, utilizando o comando:
####except mysql.connector.Error as err: e apresentando a mensagem de
####erro, com a informação do erro encontrado através do objeto err
####De seguida utilizamos a instrução finally: para fechar a ligação à base de
####dados.
##            # Confirmar que a tabela foi criada
##            print("Tabela Clientes criada com sucesso ou já existe.")
##
##    except mysql.connector.Error as err:
##        print(f"Erro ao criar a tabela: {err}")
##
##    finally:
##        if 'mycursor' in locals() and mycursor:
##            mycursor.close()
##        if 'mydb' in locals() and mydb.is_connected():
##            mydb.close()
##
####Por fim executamos a função e vamos ao mySQL para vermos a tabela
####criada.
##            
### Executar a função para criar a tabela Clientes
##criar_tabela_clientes()




##import mysql.connector
##
### Função para criar a tabela de clientes
##def criar_tabela_clientes():
##    try:
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )
##
##        if mydb.is_connected():
##            print("Conexão com a base de dados realizada com sucesso!")
##
##            mycursor = mydb.cursor()
##
##            # Criar tabela Clientes se não existir
##            mycursor.execute("""
##                CREATE TABLE IF NOT EXISTS Clientes (
##                    Cliente_Id INT AUTO_INCREMENT PRIMARY KEY,
##                    Nome VARCHAR(100),
##                    Apelido VARCHAR(100),
##                    Email VARCHAR(100) UNIQUE,
##                    Telefone VARCHAR(20),
##                    Morada VARCHAR(255),
##                    Codigo_postal VARCHAR(10),
##                    Localidade VARCHAR(100),
##                    País VARCHAR(50)
##                )
##            """)
##
##            # Confirmar que a tabela foi criada
##            print("Tabela Clientes criada com sucesso ou já existe.")
##
##    except mysql.connector.Error as err:
##        print(f"Erro ao criar a tabela: {err}")
##
##    finally:
##
##        if mydb.is_connected():
##           mycursor.close()
##           mydb.close()
####        if 'mycursor' in locals() and mycursor:
####            mycursor.close()
####        if 'mydb' in locals() and mydb.is_connected():
####            mydb.close()
##            
### Executar a função para criar a tabela Clientes
##criar_tabela_clientes()


##Conexão com a base de dados realizada com sucesso!
##Tabela Clientes criada com sucesso ou já existe.




##Slide 34
##Ainda dentro desta função vamos confirmar se a tabela foi criada e se não
##vamos verificar se existe algum erro, utilizando o comando:
##except mysql.connector.Error as err: e apresentando a mensagem de erro,
##com a informação do erro encontrado através do objeto err
##De seguida utilizamos a instrução finally: para fechar a ligação à base de
##dados.



##Consulta de dados no mysql com o Python - Slide 37
##Precisamos de ter a ligação ao mySQL ativa,
##criar um ficheiro Python de consulta e ter a
##tabela criada, de preferência com alguns registos.

##
##import mysql.connector
##
### Importa a classe Error do módulo mysql.connector para lidar com erros do MySQL.
##from mysql.connector import Error
##
##
##try
##    con = mysql.connector.connect(
##        host = 'localhost',
##        database = 'tstore',
##        user = 'root',
##        password = '')
##
##consulta_sql = "select * from clientes"
##cursor = con.cursor()
##cursor.execute(consulta_sql)
##linhas = cursor.fetchall()
##print("\nNúmero de registos encontrados: ", cursor.rowcount)
##print("\nApresentar os clientes inseridos na base de dados tstore")
##for linha in linhas:
##    print("Cliente ID: ",linha [0])
##    print("Nome: ",linha [1])
##    print("Apelido: ",linha [2])
##    print("Email: ",linha [3])
##    print("Telefone: ",linha [4])
##    print("Morada: ",linha [5])
##    print("Código Postal: ",linha [6], "\n","\n")
##
##
##expect Error as e:
##    print("Erro ao tentar aceder à tabela clientes", e)
##finally:
##    if(con.is_connected()):
##        con.close()
##        cursor.close()
##        print("A ligação ao MySQL foi encerrada com sucesso")



##
##import mysql.connector
##from mysql.connector import Error  # Importar a classe Error
##
##try:
##    con = mysql.connector.connect(
##        host='localhost',
##        database='tstore',
##        user='root',
##        password=''
##    )
##
##    if con.is_connected():
##        print("Conexão com a base de dados realizada com sucesso!")
##
##        # Criar cursor e executar consulta
##        cursor = con.cursor()
##        consulta_sql = "SELECT * FROM Clientes"
##        cursor.execute(consulta_sql)
##        linhas = cursor.fetchall()
##
##        print("\nNúmero de registos encontrados:", cursor.rowcount)
##        print("\nApresentar os clientes inseridos na base de dados 'tstore':\n")
##
##        # Loop para apresentar os resultados
##        for linha in linhas:
##            print("Cliente ID: ", linha[0])
##            print("Nome: ", linha[1])
##            print("Apelido: ", linha[2])
##            print("Email: ", linha[3])
##            print("Telefone: ", linha[4])
##            print("Morada: ", linha[5])
##            print("Código Postal: ", linha[6])
##            print("Localidade: ", linha[7])
##            print("País: ", linha[8], "\n")
##
##except Error as e:
##    print("Erro ao tentar aceder à tabela Clientes:", e)
##
##finally:
##    # Fechar cursor e conexão se existirem
##    if 'cursor' in locals() and cursor:
##        cursor.close()
##    if 'con' in locals() and con.is_connected():
##        con.close()
##        print("A ligação ao MySQL foi encerrada com sucesso.")


##Conexão com a base de dados realizada com sucesso!
##
##Número de registos encontrados: 0
##
##Apresentar os clientes inseridos na base de dados 'tstore':
##
##A ligação ao MySQL foi encerrada com sucesso.



## Slide 38
####Consulta de dados no mysql com o Python
## Receita Parte 1
##Começamos por importar o mysql.connector e a subclasse Error para
##termos a ligação ao mySQL e detectarmos possíveis erros.
##De seguida utilizamos a instrução try: … em que vamos procurar fazer a
##ligação à base de dados que desejamos, neste exemplo chama-se tstore


##
##import mysql.connector
##
### Importa a classe Error do módulo mysql.connector para lidar com erros do MySQL.
##from mysql.connector import Error
##
##
##try
##    con = mysql.connector.connect(
##        host = 'localhost',
##        database = 'tstore',
##        user = 'root',
##        password = '')



## Slide 39
##Consulta de dados no mysql com o Python
##Receita Parte 2
##Ainda dentro do bloco try vamos criar a consulta SQL que desejamos.
##Criamos o objeto cursor e executamos, solicitamos que leia todo o conteúdo
##da tabela e o apresente em linha considerando i indice de cada campo
##[0,1,2,3,4,5,6]


##try
##    con = mysql.connector.connect(
##        host = 'localhost',
##        database = 'tstore',
##        user = 'root',
##        password = '')
##
##consulta_sql = "select * from clientes"
##cursor = con.cursor()
##cursor.execute(consulta_sql)
##linhas = cursor.fetchall()
##print("\nNúmero de registos encontrados: ", cursor.rowcount)
##print("\nApresentar os clientes inseridos na base de dados tstore")
##for linha in linhas:
##    print("Cliente ID: ",linha [0])
##    print("Nome: ",linha [1])
##    print("Apelido: ",linha [2])
##    print("Email: ",linha [3])
##    print("Telefone: ",linha [4])
##    print("Morada: ",linha [5])
##    print("Código Postal: ",linha [6], "\n","\n")





## Slide 40
##Consulta de dados no mysql com o Python
##Receita Parte 3
##Precisamos também, (fora do comando try) verificar se existem erros e de
##os apresentar no terminal com o comando except Error e finalmente usar o
##comando finally para fechar a ligação, sendo que esta parte é opcional.


##expect Error as e:
##    print("Erro ao tentar aceder à tabela clientes", e)
##finally:
##    if(con.is_connected()):
##        con.close()
##        cursor.close()
##        print("A ligação ao MySQL foi encerrada com sucesso")



## Slide 41 - 42
##Inserir dados na tabela através do Python
##Inserir dados no mysql com o Python
##Precisamos de ter a ligação ao mySQL ativa,
##criar um ficheiro Python de inserção de
##dados e ter a tabela criada, de preferência com
##alguns registos.



## Testar - Errado?
##import mysql.connector
##def inserir produto():
##try:
### Conectar ao banco de dados
##mydb = mysql.connector.connect(host="localhost", user="root", password="", database="dbtestestabelas") mycursor = mydb.cursor()
### Loop para inserir múltiplos produtos
##while True:
##nome = input("Nome do produto (ou digite 'sair' para terminar): ")
##if nome.lower() == 'sair':
##break
##while True:
##try:
##descricao = input("Descrição do produto: ")
##preco = float(input("Preço do produto: "))
##quantidade = int(input("Quantidade em estoque: "))
##break # Sai do loop interno se a entrada for válida
##except ValueError:
##print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")
##sql = "INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade) VALUES (%s, %s, %s, %s)" val = (nome, descricao, preco, quantidade)
##mycursor.execute(sql, val)
##mydb.commit()
##print(mycursor.rowcount, "produto inserido.")
##except mysql.connector.Error as err:
##print("Erro ao conectar ou inserir dados: {err}")
##finally:
##if mydb.is_connected():
##mycursor.close()
##mydb.close()
##print("Conexão com o banco de dados fechada.")
### Executa a função de inserção
##inserir_produto()



#### FUNCIONA - Correto - Slide 42
##import mysql.connector
##from mysql.connector import Error
##
##def criar_base_dados():
##    con = None
##    cursor = None
##    try:
##        # Conectar ao MySQL sem especificar a base de dados
##        con = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password=""
##        )
##        if con.is_connected():
##            cursor = con.cursor()
##            # Cria a base de dados se não existir
##            cursor.execute("CREATE DATABASE IF NOT EXISTS dbtestestabelas")
##            print("Banco de dados 'dbtestestabelas' criado (ou já existente).")
##    except Error as err:
##        print(f"Erro ao criar o banco de dados: {err}")
##    finally:
##        if cursor is not None:
##            cursor.close()
##        if con is not None and con.is_connected():
##            con.close()
##            print("Conexão com o MySQL fechada.")
##
##def criar_tabela():
##    mydb = None
##    mycursor = None
##    try:
##        # Conectar à base de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="dbtestestabelas"
##        )
##        mycursor = mydb.cursor()
##
##        # Criar a tabela Produtos se não existir
##        mycursor.execute("""
##            CREATE TABLE IF NOT EXISTS Produtos (
##                id INT AUTO_INCREMENT PRIMARY KEY,
##                Produto_nome VARCHAR(100),
##                Produto_descrit TEXT,
##                Produto_preco DECIMAL(10, 2),
##                Produto_quantidade INT
##            )
##        """)
##        print("Tabela 'Produtos' criada (ou já existente).")
##        
##    except mysql.connector.Error as err:
##        print(f"Erro ao criar a tabela: {err}")
##    
##    finally:
##        if mycursor is not None:
##            mycursor.close()
##        if mydb is not None and mydb.is_connected():
##            mydb.close()
##            print("Conexão com o banco de dados fechada.")
##
##def inserir_produto():
##    mydb = None
##    mycursor = None
##    try:
##        # Conectar à base de dados que agora existe
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="dbtestestabelas"
##        )
##        mycursor = mydb.cursor()
##
##        # Loop para inserir múltiplos produtos
##        while True:
##            nome = input("Nome do produto (ou digite 'sair' para terminar): ")
##            if nome.lower() == 'sair':
##                break
##
##            # Loop para validar as entradas de descrição, preço e quantidade
##            while True:
##                try:
##                    descricao = input("Descrição do produto: ")
##                    preco = float(input("Preço do produto: "))
##                    quantidade = int(input("Quantidade em estoque: "))
##                    break  # Sai do loop se a entrada for válida
##                except ValueError:
##                    print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")
##
##            sql = ("INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade) "
##                   "VALUES (%s, %s, %s, %s)")
##            val = (nome, descricao, preco, quantidade)
##            mycursor.execute(sql, val)
##            mydb.commit()
##            print(mycursor.rowcount, "produto inserido.")
##
##    except mysql.connector.Error as err:
##        print(f"Erro ao conectar ou inserir dados: {err}")
##
##    finally:
##        if mycursor is not None:
##            mycursor.close()
##        if mydb is not None and mydb.is_connected():
##            mydb.close()
##            print("Conexão com o banco de dados fechada.")
##
### Primeiro, cria a base de dados (se não existir)
##criar_base_dados()
##
### Cria a tabela Produtos (se não existir)
##criar_tabela()
##
### Agora, insere os produtos na tabela 'Produtos'
##inserir_produto()
##
##Banco de dados 'dbtestestabelas' criado (ou já existente).
##Conexão com o MySQL fechada.
##Tabela 'Produtos' criada (ou já existente).
##Conexão com o banco de dados fechada.
##Nome do produto (ou digite 'sair' para terminar): Calças
##Descrição do produto: Calças de Ganga
##Preço do produto: 39
##Quantidade em estoque: 1
##1 produto inserido.
##Nome do produto (ou digite 'sair' para terminar): sair
##Conexão com o banco de dados fechada.




##import mysql.connector
##
##def inserir_produto():
##    try:
##        # Conectar ao banco de dados
##        mydb = mysql.connector.connect(
##            host='localhost',
##            user='root',
##            password='',
##            database='tstore')
##
##        # Loop para inserir múltiplos produtos
##        while True:
##            nome = input("Nome do produto (ou digite 'sair' para terminar): ")
##            if nome.lower() == 'sair':
##                break
##
##        while True:
##            try:
##                descricao = input("Descrição do produto: ")
##                preco = float(input("Preço do produto:"))
##                quantidade = int(input("Quantidade em stock/estoque: "))
##                break # Sai do loop interno se a entrada for válida
##            except ValueError:
##                print("Entrada inválida. Certifique--se de que o preço é um número e a quantidade é um inteiro.")
##
##
##             sql = "INSERT INTO Produtos (Produto_nome, Produto_foto, Produto_price, Produto_Quantidade) VALUES(%s, %s, %s, %s)"
##             val = (nome,foto,preco,quantidade
##             mycursor.execute(sql,val)
##                    mydb.commit()
##                    print(mycursor.rowcount, "produto inserido.")
##
##            expect mysql.connector.Error as err:
##                    print("Erro ao conectar ou inserir dados: {err}")
##                    finally:
##                    if mydb.is_connected():
##                    mycursor.close()
##                    mydb.close()
##                    print("Conexão com o banco de dados fechada.")
### Executa a função inserção
##inserir_produto()





##import mysql.connector
##
### Função para criar a tabela de produtos
##def criar_tabela_produtos():
##    try:
##        # Conectar ao banco de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )
##
##        if mydb.is_connected():
##            print("✅ Conexão com a base de dados realizada com sucesso!")
##
##            mycursor = mydb.cursor()
##
##            # Criar tabela Produtos (corrigida para evitar NULL)
##            mycursor.execute("""
##                CREATE TABLE IF NOT EXISTS Produtos (
##                    Produto_Id INT AUTO_INCREMENT PRIMARY KEY,
##                    Produto_nome VARCHAR(255) NOT NULL,
##                    Produto_foto LONGBLOB,
##                    Produto_price FLOAT NOT NULL,
##                    Produto_Quantidade INT NOT NULL
##                )
##            """)
##
##            print("✅ Tabela 'Produtos' criada com sucesso ou já existe.")
##
##    except mysql.connector.Error as err:
##        print(f"❌ Erro ao criar a tabela: {err}")
##
##    finally:
##        if 'mycursor' in locals() and mycursor:
##            mycursor.close()
##        if 'mydb' in locals() and mydb.is_connected():
##            mydb.close()
##            print("🔒 Conexão com a base de dados fechada.")
##
### Executar a função para criar a tabela
##criar_tabela_produtos()


##✅ Conexão com a base de dados realizada com sucesso!
##✅ Tabela 'Produtos' criada com sucesso ou já existe.
##🔒 Conexão com a base de dados fechada.



##FUNCIONA
##import mysql.connector
##
##def inserir_produto():
##    try:
##        # Conectar ao banco de dados
##        mydb = mysql.connector.connect(
##            host='localhost',
##            user='root',
##            password='',
##            database='tstore'
##        )
##        mycursor = mydb.cursor()
##
##        # Loop para inserir múltiplos produtos
##        while True:
##            nome = input("Nome do produto (ou digite 'sair' para terminar): ")
##            if nome.lower() == 'sair':
##                break
##
##            # Neste exemplo, não usamos uma descrição, pois a tabela não a possui.
##            # Para a foto, usaremos None, indicando que não há imagem.
##            foto = None
##
##            # Loop para validar as entradas de preço e quantidade
##            while True:
##                try:
##                    preco = float(input("Preço do produto: "))
##                    quantidade = int(input("Quantidade em stock/estoque: "))
##                    break  # Sai do loop se a entrada for válida
##                except ValueError:
##                    print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")
##
##            # Inserir o produto na tabela
##            sql = "INSERT INTO Produtos (Produto_nome, Produto_foto, Produto_price, Produto_Quantidade) VALUES (%s, %s, %s, %s)"
##            val = (nome, foto, preco, quantidade)
##            mycursor.execute(sql, val)
##            mydb.commit()
##            print(mycursor.rowcount, "produto inserido.")
##
##    except mysql.connector.Error as err:
##        print("Erro ao conectar ou inserir dados:", err)
##
##    finally:
##        if 'mycursor' in locals() and mycursor:
##            mycursor.close()
##        if 'mydb' in locals() and mydb.is_connected():
##            mydb.close()
##            print("Conexão com o banco de dados fechada.")
##
### Executa a função para inserção
##inserir_produto()
##
##Nome do produto (ou digite 'sair' para terminar): Calças
##Preço do produto: 39
##Quantidade em stock/estoque: 4
##1 produto inserido.
##Nome do produto (ou digite 'sair' para terminar): sair
##Conexão com o banco de dados fechada.





## Slide 43
##Inserir dados no mysql com o Python
##
##Receita Parte 1
##Importamos o mysql,connector
##Para que seja possível a repetição devemos começar por criar uma função
##e dentro dela no comando try vamos fazer a ligação à base de dados, criar
##um loop para ser possível inserir mais do que um registo e outro dentro dele
##para pedir a inserção de dados e verificar se é correta.
##
##
##﻿
##
##def inserir_produto():
##try:
### Conectar à base de dados
##mydb =
##mysql.connector.connect(host="localhost", user="root", password="", database="dbtestestabelas")
##mycursor mydb.cursor()
### Loop para inserir múltiplos produtos
##while True:
##nome = input("Nome do produto (ou digite 'sair' para terminar): ")
##if nome.lower() == 'sair':
##break
##while True:
##try:
##descricao = input("Descrição do produto: ")
##preco = float(input("Preço do produto: "))
##quantidade = int(input("Quantidade em estoque: "))
##break # Sai do loop interno se a entrada for válida
##except ValueError:
##print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um inteiro.")




## Slide 44
##Inserir dados no mysql com o Python
##Receita Parte 2
##Em linha com a instrução try precisamos de gerar a instrução sql e associar
##aos campos respectivos e depois executar para que os produtos sejam
##inseridos. Sendo que nesse processo vão ser percorridos os dois ciclos
##while True que vão permitir ao utilizador inserir os dados de forma correta e
##continuar a inserir novos registos
##
##sql = "INSERT INTO Produtos (Produto_nome, Produto_descrit, Produto_preco, Produto_quantidade) VALUES (%s, %s, %s, %s)" val (nome, descricao, preco, quantidade)
##mycursor.execute(sql, val)
##mydb.commit()
##print(mycursor.rowcount, "produto inserido.")




## Slide 45
##Inserir dados no mysql com o Python
##Receita Parte 3
##Precisamos também, (fora do comando try), mas dentro da função verificar
##se existem erros e de os apresentar no terminal com o comando except
##Error e usar o comando finally para fechar a ligação, sendo que esta parte é
##opcional.
##Finalmente executamos a função fora da função
##
##﻿
##
##except mysql.connector.Error as err:
##print(f"Erro ao conectar ou inserir dados: {err}")
##finally:
##if  mydb.is_connected():
##    mycursor.close()
##    mydb.close()
##print("Conexão com a base de dados fechada.")
##
### Executa a função de inserção
##inserir_produto()




## Slide 46 - 47
####Apagar dados na tabela através do Python
####Apagar dados no mysql com o Python



####Receita Parte 1
####Começamos por importar o mysql.connector e a subclasse Error
####Criamos uma função para consultar os dados pretendidos.
####Dentro da instrução try vamos fazer a ligação à base de dados que
####desejamos.


## FUNCIONOU - CÓDIGO COMPLETO - APAGAR DADOS
##import mysql.connector
##from mysql.connector import Error
##
### Função para consultar e exibir os registros da tabela Produtos
##def consultar_produtos():
##    try:
##        # Conectar à base de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="dbtestestabelas"
##        )
##
##        # Verificar se a conexão foi bem-sucedida
##        if mydb.is_connected():
##            print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##        mycursor = mydb.cursor()
##
##        # Consultar os dados da tabela Produtos
##        sql = "SELECT * FROM Produtos"
##        mycursor.execute(sql)
##
##        # Obter todos os registros obtidos na consulta
##        registros = mycursor.fetchall()
##
##        # Verificar se há registros e exibi-los
##        if registros:
##            print("Registros encontrados na tabela Produtos: \n")
##            for registro in registros:
##                id_produto, nome, descricao, preco, quantidade = registro
##                print(f"ID - {id_produto}")
##                print(f" Nome: {nome}")
##                print(f"Descrição: {descricao}")
##                print(f"Preço: {preco} Euros")
##                print(f"Quantidade: {quantidade} Unidades")
##                print("*" * 30)  # Linha separadora entre os registros
##        else:
##            print("\nNenhum registro encontrado na tabela.")
##        return registros
##
##    except Error as err:
##        print(f"Erro ao consultar a tabela: {err}")
##        return []
##    finally:
##        if mydb.is_connected():
##            mycursor.close()
##            mydb.close()
##
### Função para apagar registros da tabela Produtos
##def apagar_produto(id_produto):
##    try:
##        # Conectar à base de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="dbtestestabelas"
##        )
##
##        # Verificar se a conexão foi bem-sucedida
##        if mydb.is_connected():
##            print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##        mycursor = mydb.cursor()
##
##        # Construir a query DELETE
##        sql = "DELETE FROM Produtos WHERE id = %s"
##        val = (id_produto,)
##
##        # Executar a query
##        mycursor.execute(sql, val)
##
##        mydb.commit()  # Confirmar as alterações
##
##        print(f"Registro com ID {id_produto} apagado com sucesso!")
##
##    except Error as err:
##        print(f"Erro ao apagar o registro: {err}")
##    finally:
##        if mydb.is_connected():
##            mycursor.close()
##            mydb.close()
##
### Função principal para interação do usuário
##def main():
##    while True:
##        registros = consultar_produtos()
##        if not registros:
##            print("Não há registros para apagar.")
##            break
##
##        print("\nRegistros disponíveis:")
##        for i, registro in enumerate(registros):
##            id_produto, nome, descricao, preco, quantidade = registro
##            print(f"{i+1}. ID: {id_produto}, Nome: {nome}")
##
##        try:
##            opcao = int(input("\nDigite o número do registro que deseja apagar (ou 0 para sair): "))
##            if opcao == 0:
##                break
##
##            if opcao < 1 or opcao > len(registros):
##                print("Opção inválida.")
##                continue
##
##            id_produto_a_apagar = registros[opcao-1][0]  # Obter o ID do produto selecionado
##
##            confirmacao = input(f"Tem certeza que deseja apagar o registro {id_produto_a_apagar}? (s/n): ")
##            if confirmacao.lower() == 's':
##                apagar_produto(id_produto_a_apagar)
##            else:
##                print("Operação cancelada.")
##        except ValueError:
##            print("Entrada inválida. Por favor, digite um número inteiro.")
##
##if __name__ == "__main__":
##    main()
##
##
##
##Conexão com a base de dados realizada com sucesso!
##
##Registros encontrados na tabela Produtos: 
##
##ID - 1
## Nome: Calças
##Descrição: Calças de Ganga
##Preço: 39.00 Euros
##Quantidade: 1 Unidades
##******************************
##
##Registros disponíveis:
##1. ID: 1, Nome: Calças
##
##Digite o número do registro que deseja apagar (ou 0 para sair): 1
##Tem certeza que deseja apagar o registro 1? (s/n): s
##Conexão com a base de dados realizada com sucesso!
##
##Registro com ID 1 apagado com sucesso!
##Conexão com a base de dados realizada com sucesso!
##
##
##Nenhum registro encontrado na tabela.
##Não há registros para apagar.



## Errado - Código Completo 47- 54
##import mysql.connector
##from mysql.connector import Error
### Função para consultar e exibir os registros da tabela Produtos
##def consultar_produtos():
##try:
### Conectar à base de dados
##mydb = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="",
##    database="dbtestestabelas"
##    )
##
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##mycursor mydb.cursor()
##
### Consultar os dados da tabela Produtos
##sql = "SELECT * FROM Produtos"
##mycursor.execute(sql)
##
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##
##mycursor = mydb.cursor()
##
##
### Consultar os dados da tabela Produtos
##sql = "SELECT * FROM Produtos"
##mycursor.execute(sql)
##
##
### Obter todos os registros obtidos na consulta
##registros = mycursor.fetchall()
##
##
### Verificar se há registros e exibi-los
##if registros:
##print("Registros encontrados na tabela Produtos: \n")
##for registro in registros:
##id_produto, nome, descricao, preco, quantidade = registro
##print(f"ID - {id_produto}")
##print(f" Nome {nome}")
###print(f"Descrição - {descricao}")
##print("Preço - {preco} Euros")
##print(f" Quantidade - {quantidade} Unidades")
##print("*" * 30) # Linha separadora entre os registros
##else:
##print("\nNenhum registro encontrado na tabela.")
##return registros
##
##
##except Error as err:
##print(f"Erro ao consultar a tabela: {err}")
##return []
##finally:
##if  mydb.is_connected():
##    mycursor.close()
##    mydb.close()
##
##
### Função para apagar registros da tabela Produtos
##def apagar produto(id_produto):
##try:
### Conectar à base de dados
##mydb = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="
##    database="dbtestestabelas"
##    )
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##mycursor = mydb.cursor()
##
##
### Construir a query DELETE
##sql = "DELETE FROM Produtos WHERE Produto_id = %s"
##val = (id_produto,)
##
##
### Executar a query
##mycursor.execute(sql, val)
##
##
##mydb.commit() # Confirmar as alterações
##
##
##print(f" Registro com ID {id_produto} apagado com sucesso!")
##
##
##except Error as err:
##print(f" Erro ao apagar o registro: {err}")
##finally:
##if mydb.is_connected():
##mycursor.close()
##mydb.close()
##
##
### Função principal para interação do utilizador
##def main():
##while True:
##registros consultar_produtos()
##if not registros:
##print("Não há registros para apagar.")
##break
##
##
##print("\nRegistros disponíveis:")
##for i, registro in enumerate(registros):
##try:
##id_produto, nome, descricao, preco, quantidade = registro
##print(f" (i+1). ID: {id_produto}, Nome: {nome}")
##
##try:
##opcao = int(input("\nDigite o número do registro que deseja apagar (ou 0 para sair): "))
##if opcao == 0:
##break
##
##
##if opcao < 1 or opcao > len(registros):
##print("Opção inválida.")
##continue
##
##
##id_produto_a_apagar registros [opcao-1][0] # Obter o ID do produto selecionado
##
##
##confirmacao = input(f"Tem certeza que deseja apagar o registro [id_produto_a_apagar}? (s/n): ")
##if confirmacao.lower() == 's':
##apagar_produto(id_produto_a_apagar)
##else:
##print("Operação cancelada.")
##except ValueError:
##print("Entrada inválida. Por favor, digite um número inteiro.")
##
##
##
##if _name_ == "___main____":
##main()


##import mysql.connector
##from mysql.connector import Error
##
### Função para consultar e exibir os registos da tabela Produtos
##def consultar_produtos():
##    try:
##        # Conectar à base de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )




## Slide 48
##Apagar dados no mysql com o Python
##Receita Parte 2
##Ainda dentro da instrução try, verificamos se a conexão foi bem sucedida,
##criamos o cursor e a instrução SQL para fazer a consulta da tabela que
##desejamos.


### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##mycursor mydb.cursor()
##
### Consultar os dados da tabela Produtos
##sql = "SELECT * FROM Produtos"
##mycursor.execute(sql)



## Slide 48
##Apagar dados no mysql com o Python
##Receita Parte 3
##Ainda dentro da instrução try, verificamos se a conexão foi bem sucedida,
##criamos o cursor e a instrução SQL para fazer a consulta da tabela que
##desejamos.
##Criamos um objeto (variável) que vai guardar todos os registos encontrados
##usando o método fetchall()


### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##
##mycursor = mydb.cursor()
##
##
### Consultar os dados da tabela Produtos
##sql = "SELECT * FROM Produtos"
##mycursor.execute(sql)
##
##
### Obter todos os registros obtidos na consulta
##registros = mycursor.fetchall()

## Slide 50
##Apagar dados no mysql com o Python
##Receita Parte 4
##Verificamos se existem registos e se sim apresentamos todos os registos
##utilizando um ciclo for que vai correr todos os registos que encontrar e
##apresentar a informação no terminal. caso não encontre apresenta essa
##informação. No final do ciclo avança para a próxima etapa


### Verificar se há registros e exibi-los
##if registros:
##print("Registros encontrados na tabela Produtos: \n")
##for registro in registros:
##id_produto, nome, descricao, preco, quantidade = registro
##print(f"ID - {id_produto}")
##print(f" Nome {nome}")
###print(f"Descrição - {descricao}")
##print("Preço - {preco} Euros")
##print(f" Quantidade - {quantidade} Unidades")
##print("*" * 30) # Linha separadora entre os registros
##else:
##print("\nNenhum registro encontrado na tabela.")
##return registros




## Slide 51
##Apagar dados no mysql com o Python
##Receita Parte 5
##Precisamos também, (fora do comando try), mas dentro da função verificar
##se existem erros e de os apresentar no terminal com o comando except
##Error e usar o comando finally para fechar a ligação, sendo que esta parte é
##opcional.

##except Error as err:
##print(f"Erro ao consultar a tabela: {err}")
##return []
##finally:
##if  mydb.is_connected():
##    mycursor.close()
##    mydb.close()



## Slide 52
##Apagar dados no mysql com o Python
##Receita Parte 6
##Precisamos também de criar uma função para
##apagar registos.
##
##Criamos a ligação à base de dados criamos o query
##SQL para apagar registos, usando como valor a chave principal,
##Executamos o query e confirmamos.



### Função para apagar registros da tabela Produtos
##def apagar produto(id_produto):
##try:
### Conectar à base de dados
##mydb = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="
##    database="dbtestestabelas"
##    )
##
### Verificar se a conexão foi bem-sucedida
##if mydb.is_connected():
##print(f"Conexão com a base de dados realizada com sucesso!\n")
##
##mycursor = mydb.cursor()
##
##
### Construir a query DELETE
##sql = "DELETE FROM Produtos WHERE Produto_id = %s"
##val = (id_produto,)
##
##
### Executar a query
##mycursor.execute(sql, val)
##
##
##mydb.commit() # Confirmar as alterações
##
##
##print(f" Registro com ID {id_produto} apagado com sucesso!")
##
##
##except Error as err:
##print(f" Erro ao apagar o registro: {err}")
##finally:
##if mydb.is_connected():
##mycursor.close()
##mydb.close()




## Slide 53
##Apagar dados no mysql com o Python
##Receita Parte 7
##De seguida criamos uma função principal que vai usar as anteriores para
##consultar a tabela e apagar os registos




### Função principal para interação do utilizador
##def main():
##while True:
##registros consultar_produtos()
##if not registros:
##print("Não há registros para apagar.")
##break
##
##
##print("\nRegistros disponíveis:")
##for i, registro in enumerate(registros):
##try:
##id_produto, nome, descricao, preco, quantidade = registro
##print(f" (i+1). ID: {id_produto}, Nome: {nome}")
##
##try:
##opcao = int(input("\nDigite o número do registro que deseja apagar (ou 0 para sair): "))
##if opcao == 0:
##break
##
##
##if opcao < 1 or opcao > len(registros):
##print("Opção inválida.")
##continue
##
##
##id_produto_a_apagar registros [opcao-1][0] # Obter o ID do produto selecionado
##
##
##confirmacao = input(f"Tem certeza que deseja apagar o registro [id_produto_a_apagar}? (s/n): ")
##if confirmacao.lower() == 's':
##apagar_produto(id_produto_a_apagar)
##else:
##print("Operação cancelada.")
##except ValueError:
##print("Entrada inválida. Por favor, digite um número inteiro.")




## Slide 54
##Apagar dados no mysql com o Python
##Receita Parte 8
##Por fim executamos essa função dentro de uma condição em que é usada
##para garantir que o código dentro desse bloco seja executado apenas
##quando o arquivo Python é executado diretamente e não quando ele é
##importado como um módulo em outro script.

##if _name_ == "___main____":
##main()


##r__name__:
##É uma variável especial no Python que recebe o valor "__main__" quando o
##script é executado diretamente.
##Caso o script seja importado, __name__ terá o nome do módulo (ou seja, o
##nome do arquivo sem a extensão .py).





## Slide 55
##Criar Aplicação para inserir dados na tabela - Slide 56
##Podemos usar a biblioteca thinker para criar essa aplicação
##
##Para tudo funcionar é importante termos o localhost
##e a ligação ao mySQL ativa.
##Criamos um novo ficheiro Python e importamos
##as bibliotecas necessárias:


##import tkinter as tk # Importa o módulo tkinter
##from tkinter import messagebox # Para apresentar mensagens
##import mysql.connector # Para interagir com MySQL
##import re # Biblioteca para validação de email e telefone



## Slide 57
##De seguida criamos a função para inserir dados:
### Função para validar e inserir dados na tabela Clientes
##def inserir_dados():
##
##"""
##Este bloco de código recolhe os dados introduzidos pelo
##utilizador em várias entradas de texto,
##utilizando o método .get() para obter o texto de cada campo.
##O método .strip() remove os espaços em branco no início ou no fim dos valores
##introduzidos, garantindo que os dados recolhidos estejam
##limpos e prontos para serem processados.
##"""
##
##nome = entry_nome.get().strip()
##apelido = entry_apelido.get().strip()
##email = entry_email.get().strip()
##telefone = entry_telefone.get().strip()
##morada entry_morada.get().strip()
##codigo_postal = entry_codigo_postal.get().strip()
##localidade = entry_localidade.get().strip()
##pais = entry_pais.get().strip()



## Slide 58
##Ainda dentro dessa função precisamos de fazer a validação de dados.
##neste caso verificarmos se foram preenchidos os campos obrigatórios e se
##o email e telefone são válidos.


### Validações dos campos obrigatórios
##if not nome or not apelido or not email or not telefone or not morada or not codigo_postal:
##messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser preenchidos!")
##return
##
##
### Validação de email
##if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
##messagebox.showerror("Erro", "O email não é válido!")
##return
##
##
### Validação de telefone
##if not telefone.isdigit() or len(telefone) < 9:
##messagebox.showerror("Erro", "O telefone deve conter apenas números e ter pelo menos 9 dígitos!")
##return



## Slide 59
##Ainda dentro dessa função precisamos de criar a ligação à base de dados,
##criar o cursor para interagir com a mesma.



### Inserir dados na base de dados tstore
##try:
### Conectar ao banco de dados
##mydb = mysql.connector.connect(
##host="localhost",
##user="root",
##password=""
##database="tstore"
##)
##mycursor = mydb.cursor() # Cria um cursor para executar comandos SQL na base de dados


##Depois vamos usar um objeto (variável) que vai inserir os dados usando SQL.



## Slide 60
##Ainda dentro dessa função solicitamos que após os dados serem enviados
##a aplicação limpe os dados para que possam ser adicionados novos clientes se quisermos.


### Limpar os campos no interface gráfico
##entry_nome.delete(0, tk.END)
##entry_apelido.delete(0, tk. END)
##entry_email.delete(0, tk. END)
##entry_telefone.delete(0, tk.END)
##entry_morada.delete(0, tk.END)
##entry_codigo_postal.delete(0, tk.END)
##entry_localidade.delete(0, tk.END)
##entry_pais.delete(0, tk.END)
##
##
####Também dentro dessa função, precisamos de tratar os erros de inserção e
####permitir que a ligação à base de dados seja encerrada.
##
##
### Tratar erros de inserção e garante o encerramento da conexão com a base de dados.
##except mysql.connector.Error as err:
##messagebox.showerror("Erro", f"Erro ao inserir os dados: {err}")
##finally:
##if mydb.is_connected():
##mycursor.close()
##mydb.close()


## Slide 61
####Fora da função vamos então gerar a aplicação, começando por criar a
####janela, incluindo titulo, dimensões, cor de fundo e transparência, se
####desejarmos
##
##
### Criar a interface gráfica
##janela = tk.Tk()
##janela.title("INSERIR DADOS - TABELA CLIENTES")
##janela.geometry("700x600")
##janela.configure(bg="darkblue")
##janela.wm_attributes('-alpha', 0.9) # Janela semi-transparente
##
##
####Depois adicionamos duas labels de títulos que irão aparecer no topo da
####aplicação
##
##
### Títulos
##titulo = tk.Label(janela, text="Inserir Dados - Clientes", font=("Verdana", 14, "bold"), fg="white", bg="darkblue")
##titulo.grid(row=0, column=0, columnspan=2, pady=10)
##subtitulo = tk.Label (janela, text="Deve preencher todos os campos", font=("Verdana", 12, "bold"), fg="white", bg="darkblue")
##subtitulo.grid(row=1, column=0, columnspan=2, pady=5)




#### Slide 62
####Criamos abaixo a função geral para criar os diversos campos, utilizando
####uma grelha para ficarem posicionados corretamente.
##
### Função para criar campo com grid
##def criar_campo(rotulo, linha):
##label = tk.Label (janela, text=rotulo, font=("Verdana", 11), fg="white", bg="darkblue")
##label.grid(row=linha, column=0, padx=10, pady=5, sticky="e")
##entry = tk.Entry(janela, width=40)
##entry.grid(row=linha, column=1, padx=10, pady=5, sticky="w")
##return entry



##﻿Fora dessa função criamos então os campos para a inserção dos dados e
##a label correspondente



##### Criar os campos de entrada
##entry_nome = criar_campo("Nome:", 2)
##entry_apelido = criar_campo("Apelido:", 3)
##entry_email = criar_campo("Email:", 4)
##entry_telefone = criar_campo("Telefone:", 5)
##entry_morada = criar_campo("Morada:", 6)
##entry_codigo_postal = criar_campo("Código Postal:", 7)
##entry_localidade = criar_campo("Localidade:", 8)
##entry_pais = criar_campo("País:", 9)





#### Slide 63
##Criamos então o botão para enviar os dados inseridos nas caixas de texto
##pelo utilizador.


### Botão para inserir dados
##"""Este bloco de código cria um botão na interface gráfica que,
##quando pressionado, chama a função `inserir_dados`.
##O botão é configurado com o seguinte:
##- Texto: "ENVIAR DADOS", exibido no botão.
##- Fonte: "Verdana" com tamanho 10 e estilo "negrito" (bold).
##- Cor de fundo (bg): azul.
##Cor do texto (fg): branco.
##- Comando (command): associa o clique no botão à função `inserir_dados`.
##
##O botão é posicionado usando o método grid`, com os seguintes parâmetros:
##- `row=10: Define que o botão será colocado na décima linha do layout.
##- column=0: Define que o botão estará na primeira coluna.
##- `columnspan=2`: Faz o botão ocupar o espaço de duas colunas, centralizando-o.
##-pady=20: Adiciona um espaçamento vertical de 20 pixels ao redor do botão.
##"""
##botao_inserir = tk.Button(janela, text="ENVIAR DADOS", font=("Verdana", 10, "bold"), bg="blue", fg="white", command=inserir_dados)
##botao_inserir.grid(row-10, column-0, columnspan-2, pady-20)


##E por fim executamos o loop geral que vai fazer o programa correr até que
##a janela seja fechada.
##
### Iniciar a aplicação
##janela.mainloop()



## Código Completo e Corrigido - Slide 56 até 63
##import tkinter as tk  # Importa o módulo tkinter
##from tkinter import messagebox  # Para apresentar mensagens
##import mysql.connector  # Para interagir com MySQL
##import re  # Biblioteca para validação de email e telefone
##
##
## Função para validar e inserir dados na tabela Clientes
##def inserir_dados():
##    # Recolher os dados do formulário
##    nome = entry_nome.get().strip()
##    apelido = entry_apelido.get().strip()
##    email = entry_email.get().strip()
##    telefone = entry_telefone.get().strip()
##    morada = entry_morada.get().strip()
##    codigo_postal = entry_codigo_postal.get().strip()
##    localidade = entry_localidade.get().strip()
##    pais = entry_pais.get().strip()
##
##    # Validações dos campos obrigatórios
##    if not nome or not apelido or not email or not telefone or not morada or not codigo_postal:
##        messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser preenchidos!")
##        return
##
##    # Validação de email
##    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
##        messagebox.showerror("Erro", "O email não é válido!")
##        return
##
##    # Validação de telefone
##    if not telefone.isdigit() or len(telefone) < 9:
##        messagebox.showerror("Erro", "O telefone deve conter apenas números e ter pelo menos 9 dígitos!")
##        return
##
##    # Inserir dados na base de dados tstore
##    try:
##        # Conectar ao banco de dados
##        mydb = mysql.connector.connect(
##            host="localhost",
##            user="root",
##            password="",
##            database="tstore"
##        )
##        mycursor = mydb.cursor()  # Cria um cursor para executar comandos SQL
##
##        # Query de inserção corrigida (garantindo que 'País' seja o nome correto da coluna)
##        sql = "INSERT INTO Clientes (Nome, Apelido, Email, Telefone, Morada, Codigo_postal, Localidade, País) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
##        valores = (nome, apelido, email, telefone, morada, codigo_postal, localidade, pais)
##
##        mycursor.execute(sql, valores)
##        mydb.commit()  # Confirma a inserção
##
##        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
##
##        # Limpar os campos no interface gráfico
##        entry_nome.delete(0, tk.END)
##        entry_apelido.delete(0, tk.END)
##        entry_email.delete(0, tk.END)
##        entry_telefone.delete(0, tk.END)
##        entry_morada.delete(0, tk.END)
##        entry_codigo_postal.delete(0, tk.END)
##        entry_localidade.delete(0, tk.END)
##        entry_pais.delete(0, tk.END)
##
##    except mysql.connector.Error as err:
##        messagebox.showerror("Erro", f"Erro ao inserir os dados: {err}")
##
##    finally:
##        if mydb.is_connected():
##            mycursor.close()
##            mydb.close()
##
##
## Criar a interface gráfica
##janela = tk.Tk()
##janela.title("INSERIR DADOS - TABELA CLIENTES")
##janela.geometry("700x600")
##janela.configure(bg="darkblue")
##janela.wm_attributes('-alpha', 0.9)  # Janela semi-transparente
##
## Títulos
##titulo = tk.Label(janela, text="Inserir Dados - Clientes", font=("Verdana", 14, "bold"), fg="white", bg="darkblue")
##titulo.grid(row=0, column=0, columnspan=2, pady=10)
##subtitulo = tk.Label(janela, text="Deve preencher todos os campos", font=("Verdana", 12, "bold"), fg="white", bg="darkblue")
##subtitulo.grid(row=1, column=0, columnspan=2, pady=5)
##
##
## Função para criar campos de entrada
##def criar_campo(rotulo, linha):
##    label = tk.Label(janela, text=rotulo, font=("Verdana", 11), fg="white", bg="darkblue")
##    label.grid(row=linha, column=0, padx=10, pady=5, sticky="e")
##    entry = tk.Entry(janela, width=40)
##    entry.grid(row=linha, column=1, padx=10, pady=5, sticky="w")
##    return entry
##
##
## Criar os campos de entrada
##entry_nome = criar_campo("Nome:", 2)
##entry_apelido = criar_campo("Apelido:", 3)
##entry_email = criar_campo("Email:", 4)
##entry_telefone = criar_campo("Telefone:", 5)
##entry_morada = criar_campo("Morada:", 6)
##entry_codigo_postal = criar_campo("Código Postal:", 7)
##entry_localidade = criar_campo("Localidade:", 8)
##entry_pais = criar_campo("País:", 9)
##
## Botão para inserir dados
##botao_inserir = tk.Button(janela, text="ENVIAR DADOS", font=("Verdana", 10, "bold"), bg="blue", fg="white", command=inserir_dados)
##botao_inserir.grid(row=10, column=0, columnspan=2, pady=20)
##
## Iniciar a aplicação
##janela.mainloop()






## Slide 65
##Criar base de dados em excel através do Python 
##Criar ligação python excel
##Receita:
##Primeiro precisamos de instalar as bibliotecas necessárias
##Na linha de comandos precisamos de dar a instrução:
##    pip install openpyxl
##
##E de seguida:
##pip install pandas openpyxl



    
## Slide 66
##Criar ficheiro excel e tabela dentro do ficheiro criado
##Para criarmos um ficheiro excel e dentro dele uma tabela podemos usar o
##Python, desta forma:

    
##import pandas as pd
##
### Criar um DataFrame com os dados
##dados = {
##    "Nome": ["Ana", "Bruno", "Carlos"],
##    "Idade": [23, 35, 29],
##    "Cidade": ["Lisboa","Porto","Coimbra"]
##    }
##
##tabela = pd.DataFrame(dados)
##
##
### Salvar o DataFrame como um arquivo Excel
##tabela.to_excel("DB_Excel.xlsx", index=False)
##
##print("Arquivo 'tabela.xlsx' criado com sucesso!")



### Correção 1
##import pandas as pd
##
### Criar um DataFrame com os dados
##dados = {
##    "Nome": ["Ana", "Bruno", "Carlos"],
##    "Idade": [23, 35, 29],
##    "Cidade": ["Lisboa", "Porto", "Coimbra"]
##}
##
##tabela = pd.DataFrame(dados)
##
### Salvar o DataFrame como um arquivo Excel
##tabela.to_excel("DB_Excel.xlsx", index=False)
##
##print("Arquivo 'DB_Excel.xlsx' criado com sucesso!")

##Arquivo 'DB_Excel.xlsx' criado com sucesso!



## Slide 67
##Adicionar Dados a uma Folha de Excel Existente
##Se quisermos adicionar novos registos a esta tabela podemos fazer
##assim:
##
##import pandas as pd
### Ler a folha de Excel existente
##arquivo = "DB_Excel.xlsx"
##tabela = pd.read_excel (arquivo)
### Adicionar novos dados ao DataFrame
##novos_dados = pd.DataFrame({
##"Nome": ["Diana", "Eduardo"],
##"Idade": [30, 28],
##"Cidade": ["Aveiro", "Faro"]
##})
##tabela_atualizada = pd.concat([tabela, novos_dados], ignore_index=True)
### Salvar a folha atualizada
##tabela_atualizada.to_excel (arquivo, index=False)
##print(f"Novos dados adicionados ao arquivo '{arquivo}'.")



##### Correção 2
##import pandas as pd
##import os
##
### Definir o nome do arquivo Excel
##arquivo = "DB_Excel.xlsx"
##
### Verificar se o arquivo já existe
##if os.path.exists(arquivo):
##    # Ler a folha de Excel existente
##    tabela = pd.read_excel(arquivo)
##else:
##    # Se o arquivo não existir, criar um DataFrame vazio
##    tabela = pd.DataFrame(columns=["Nome", "Idade", "Cidade"])
##
### Adicionar novos dados ao DataFrame
##novos_dados = pd.DataFrame({
##    "Nome": ["Diana", "Eduardo"],
##    "Idade": [30, 28],
##    "Cidade": ["Aveiro", "Faro"]
##})
##
### Concatenar os dados existentes com os novos dados
##tabela_atualizada = pd.concat([tabela, novos_dados], ignore_index=True)
##
### Remover duplicatas com base na coluna "Nome"
##tabela_atualizada = tabela_atualizada.drop_duplicates(subset="Nome", keep="last")
##
### Salvar a folha atualizada de volta no arquivo
##tabela_atualizada.to_excel(arquivo, index=False)
##
### Confirmar que os dados foram adicionados
##print(f"Novos dados adicionados ao arquivo '{arquivo}'.")

##Novos dados adicionados ao arquivo 'Clientes_Atualizados.xlsx'.


## Slide 68
##Adicionar Dados a uma Folha de Excel Existente
##Se quisermos adicionar novos registos a esta tabela podemos fazer
##assim:



##import pandas as pd
##
### Definir o nome do arquivo Excel
##arquivo = "DB_Excel.xlsx"
##
### Ler o arquivo Excel
##tabela = pd.read_excel(arquivo)
##
### Alterar valores no DataFrame
##tabela.loc[tabela["Nome"] == "Ana", "Idade"] = 24  # Atualiza a idade da Ana
##tabela.loc[tabela["Nome"] == "Carlos", "Cidade"] = "Guimarães"  # Atualiza a cidade de Carlos
##
### Salvar as alterações no mesmo arquivo
##tabela.to_excel(arquivo, index=False)
##
### Confirmar que os dados foram atualizados
##print(f"Dados atualizados no arquivo '{arquivo}'.")


##### Correção 3
##import pandas as pd
##
### Definir o nome do arquivo Excel
##arquivo = "DB_Excel.xlsx"
##
### Ler o arquivo Excel
##tabela = pd.read_excel(arquivo)
##
### Alterar valores no DataFrame
##tabela.loc[tabela["Nome"] == "Ana", "Idade"] = 24  # Atualiza a idade da Ana
##tabela.loc[tabela["Nome"] == "Carlos", "Cidade"] = "Guimarães"  # Atualiza a cidade de Carlos
##
### Salvar as alterações no mesmo arquivo
##tabela.to_excel(arquivo, index=False)
##
### Confirmar que os dados foram atualizados
##print(f"Dados atualizados no arquivo '{arquivo}'.")





# Slide 69
##Criar várias abas numa nova folha Excel
##Se quisermos criar uma folha de cálculo com abas personalizadas
##podemos fazer assim:
##    ﻿
##import pandas as pd
### Criar dois DataFrames
##dados1 = pd.DataFrame({
##    "Nome": ["Ana", "Bruno", "Carlos"],
##    "Idade": [23, 35, 29]
##})
##
##dados2 = pd.DataFrame({
##"Produto": ["Caneta", "Caderno", "Lápis"],
##"Preço": [1.5, 2.0, 0.5]
##})
##
### Salvar os DataFrames em abas separadas
##with pd.ExcelWriter("multi_abas.xlsx") as writer:
##dados1.to_excel (writer, sheet_name="Pessoas", index=False)
##dados2.to_excel (writer, sheet_name="Produtos", index=False)
##print("Arquivo 'multi_abas.xlsx' criado com sucesso com múltiplas abas.")


##### Correção 4
##import pandas as pd
##
### Criar dois DataFrames
##dados1 = pd.DataFrame({
##    "Nome": ["Ana", "Bruno", "Carlos"],
##    "Idade": [23, 35, 29]
##})
##
##dados2 = pd.DataFrame({
##    "Produto": ["Caneta", "Caderno", "Lápis"],
##    "Preço": [1.5, 2.0, 0.5]
##})
##
### Salvar os DataFrames em abas separadas
##with pd.ExcelWriter("multi_abas.xlsx") as writer:
##    dados1.to_excel(writer, sheet_name="Pessoas", index=False)
##    dados2.to_excel(writer, sheet_name="Produtos", index=False)
##
### Confirmar que o arquivo foi criado com sucesso
##print("Arquivo 'multi_abas.xlsx' criado com sucesso com múltiplas abas.")


##Anaconda e ambientes de desenvolvimento para gestão de bases de dados - Slide 70
##O que é Anaconda?
##
##
##Anaconda é uma distribuição open-source para Python e R*, voltada para
##análise e recolha de dados e machine learning.
##Inclui uma série de ferramentas e pacotes úteis (pandas, numpy, scipy,
##jupyter).
##Facilita a gestão de pacotes e ambientes de desenvolvimento.
##Permite criar ambientes isolados para diferentes projetos, evitando
##conflitos de dependências.
##
##R é uma linguagem de programação e um ambiente de software livre para
##computação estatística e gráficos. É amplamente utilizado entre estatísticos e
##cientistas de dados para análise de dados, modelagem estatística e
##visualização de informações.



##Porque usar o Anaconda?
##Facilidade de Instalação: Permite instalar vários pacotes e bibliotecas
##essenciais com uma única configuração.
##
##Gestão de Pacotes: A ferramenta conda permite instalar, atualizar e gerir
##pacotes de forma simples.
##
##Ambientes Isolados: Ideal para trabalhar com projetos que utilizam
##diferentes versões de pacotes ou de Python.
##
##Instalar Anaconda
##Fazer o download em anaconda.com/download.
##Executar o instalador e seguir as instruções.
##Verificar a instalação abrindo o Anaconda prompt de comando e digitar
##conda --version.


##Usar Anaconda
##Requisitos para usar:
##1. Instalar o Anaconda ou Miniconda:
##Certifique-se de que o Anaconda está instalado corretamente no
##seu sistema.
##Se desejar uma versão mais leve, pode instalar o Miniconda, que
##oferece funcionalidades similares com menos ferramentas
##predefinidas


##Instalação e uso
##Requisitos para usar:
##2. Configuração do Terminal/Shell:
##No Windows: Adicione o conda ao PATH do sistema ou use o
##Anaconda Prompt, que já vem configurado.
##No macOS/Linux: O instalador do Anaconda geralmente configura o
##conda automaticamente no terminal. Verifique isso com o comando
##conda --version.



##Instalação e uso
##Requisitos para usar:
##3. Testar a Instalação:
##Depois de instalar, execute conda --version no terminal. Se o
##comando funcionar e exibir a versão, o Anaconda está corretamente
##configurado.
##4. Ligação à Internet:
##Para descarregarmos pacotes ao criar ou configurar um ambiente pela
##primeira vez, precisamos de estar ligados à internet
##5. Conda Atualizado (Opcional):
##Antes de criar ambientes, é recomendável atualizar o conda para
##evitar problemas de compatibilidade. Para tal usamos a instrução:
##conda update conda
##
##
##Instalação e uso
##Requisitos para usar:
##6. Espaço em Disco:
##Certifique-se de que há espaço suficiente no disco para criar novos
##ambientes e instalar bibliotecas. O Anaconda pode usar uma
##quantidade considerável de espaço dependendo das ferramentas
##instaladas.
##7. Pacote Python (Caso de Miniconda):
##Se estiver a usar o Miniconda, pode ser necessário especificar a
##versão do Python na criação do ambiente, já que o Miniconda não
##inclui o Python por padrão.
##8. Permissões de Sistema (em algumas plataformas):
##No Linux/macOS, pode ser necessário alterar permissões de pastas
##se ele estiver instalado em diretórios protegidos.
##
##
##O que são Ambientes de Desenvolvimento?
##Um ambiente de desenvolvimento é um espaço controlado onde podemos
##configurar bibliotecas, versões do Python, e ferramentas específicas para um
##projeto.
##Vantagem: Ao isolar cada projeto em seu próprio ambiente, evita-se conflitos
##entre diferentes versões de pacotes.
##Exemplo: Um projeto pode requerer Python 3.8 e outro, Python 3.10 — com
##ambientes, ambos podem coexistir sem problemas.
##
##
##
##Exemplos
##Criação de um ambiente no prompt do Anaconda;
##Exemplo: conda create -n meu_ambiente python=3.9 -y
##
##-n indica o nome do ambiente que estamos a criar. No exemplo, o ambiente é
##chamado de meu_ambiente. python=3.9 especifica a versão do Python que será
##usada no ambiente, garantindo compatibilidade com bibliotecas ou projetos que
##exigem essa versão.
##
##
##Ativação de um ambiente com o prompt do Anaconda:
##conda activate meu_ambiente
##
##
##O comando conda activate meu_ambiente ativa o ambiente especificado,
##configurando o terminal para trabalhar com as bibliotecas e configurações do
##ambiente. Se o ambiente não foi criado, o sistema retornará um erro indicando
##que o ambiente não existe. É necessário criá-lo primeiro com conda create.
##
##conda env list # Lista os ambientes criados
##conda remove -n meu_ambiente --all # Remove o ambiente
##
##
##Criar um ambiente de desenvolvimento no navegador - Slide 80


##
##Spyder – O Ambiente de Desenvolvimento Científico
##
##Spyder é uma IDE otimizada para gestão de bases de dados, com
##funcionalidades de depuração, exploração de variáveis, e suporte completo
##para pacotes científicos.
##Recursos principais:
##Editor de código com realce de sintaxe.
##Integração com o IPython Console.
##Visualizador de variáveis (útil para manipulação de dados em tempo
##real)
##
##
##conda install spyder
##Para correr o IDE basta escrever no prompt spyder.
##
##
##Spyder – O Ambiente de Desenvolvimento
##Científico
##Spyder é uma IDE otimizada para gestores de bases de dados, com
##funcionalidades de depuração, exploração de variáveis, e suporte completo
##para pacotes científicos.
##Recursos principais:
##Editor de código com realce de sintaxe.
##Integração com o IPython Console.
##Visualizador de variáveis (útil para manipulação de dados em tempo
##real).
##
##
##conda install spyder
##


##Machine Learning e Python - Slide 83
##Introdução ao Machine Learning no Python
##Machine Learning ou aprendizagem de máquina, permite que as
##máquinas inteligentes aprendam a partir de dados, sem serem
##explicitamente programadas. Isso tem inúmeras aplicações, como:
##Detecção de fraudes
##Reconhecimento de voz
##Automóveis inteligentes
##Drones Inteligentes
##Recomendação de produtos/ serviços (o famoso algoritmo das redes
##sociais).
##Análise de emoções
##...
##
##
##Exemplo com Teachable Machine
##Vamos ver como treinar um modelo de Learning Machine utilizando
##Teachable Machine
##
##
##Tal como em outros workflows de machine learning, primeiro precisamos
##de obter dados, começamos por escolher que tipo de projeto queremos
##criar. Aprendizagem com imagens/vídeo, audio ou posturas
##
##
##Precisamos de criar classes de objetos. Tal como na programação
##precisamos de ter pelo menos 2 situações que possam ser comparáveis e
##processadas. Por exemplo. Emoção alegre vs Emoção triste. Também
##podemos adicionar outras categorias ex. Emoção de raiva.
##
##
##Para que o computador aprenda a identificar cada categoria precisamos
##de um número mínimo de 30 exemplos, o ideal é serem 50 para cada
##categoria. Neste caso vamos usar a webcam para simular duas situações
##simples: Com óculos vs sem òculos
##
##
##
##Precisamos então de trainer o programa, usar as emoções e verificar se
##são identificadas na grande maioria dos casos. Se não forem, precisamos
##de treinar o programa de novo, até termos os resultados de identificação
##desejados.
##
##
##Se usarmos áudio, precisamos de ter para cada categoria cerca de 20 de
##segundos de exemplo no mínimo. Aqui está um exemplo de falha ao
##reconhecer sons diferentes.
##
##
##
##Integração Teachable Machine com Python
##Exemplo
##https://youtu.be/knTjhPmW5FQ?si=5Rm_FknNoUzHNWN3
##
##
##Machine Learning Conceitos fundamentais
##
##O processo de aprendizagem de máquina envolve as seguintes etapas:
##Preparação dos Dados: Limpeza, transformação e seleção dos dados
##relevantes.
##Seleção do Algoritmo: Escolha do algoritmo adequado para o
##problema em questão.
##Treino do Modelo: Treino do modelo usando amostras
##representativas..
##Teste do Modelo: Avaliação do desempenho do modelo usando dados
##de teste.
##Utilização do Modelo: Utilização do modelo treinado para fazer
##previsões.


##GITHUB E IA - Slide 93 - 98
##O que é GitHub?
##GitHub é uma plataforma online onde podemos armazenar, partilhar e
##colaborar em projetos de código, com funcionalidades como gestão
##de versões, revisão de código e integração contínua.
##Gestão de versões é uma forma de guardar diferentes versões de um
##projeto, acompanhar mudanças e trabalhar em equipa, sem confundir
##alterações. Não está ligada às versões do Python, mas sim ao código que
##escrevemos.
##Revisão de código: Processo de verificar o código escrito por outra pessoa
##para garantir qualidade e encontrar erros.
##Integração contínua: Método de combinar frequentemente alterações no
##código num repositório, testando automaticamente para evitar problemas.
##
##
##GitHub e GitHub Desktop
##GitHub é uma plataforma online para armazenar, partilhar e colaborar
##em projetos de programação.
##GitHub Desktop é uma aplicação que facilita o uso do Git através de
##uma interface gráfica.
##Juntos, permitem gerir versões de projetos e colaborar sem complicações.
##Git é uma ferramenta para gerir versões de código no computador.
##GitHub é uma plataforma online que usa o Git para facilitar a colaboração
##e partilha de projetos.
##
##
##
##Conceitos Básicos de Git
##Repositório - Um local onde o projeto é guardado, com todas as versões
##e alterações do código.
##Commit - Um registo das alterações feitas no código, como uma
##"fotografia" do trabalho até ao momento.
##Branch - Uma versão paralela do projeto que permite testar ou
##desenvolver algo novo sem alterar o código principal.
##Merge - O processo de juntar uma branch ao código principal após
##terminar e rever as alterações.
##Histórico - Uma lista de todos os commits, que mostra quem fez o quê e
##quando.
##
##
##Gestão de Versões
##
##O que é?
##Uma forma de acompanhar alterações num projeto, guardando diferentes
##versões do código.
##Porquê usar?
##Permite recuperar trabalhos antigos, evitar conflitos entre programadores e
##manter o código organizado.
##Exemplo prático
##Editar um ficheiro Python, guardar como commit e visualizar o histórico
##das mudanças no Git.


