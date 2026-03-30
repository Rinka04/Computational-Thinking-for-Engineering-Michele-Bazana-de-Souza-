"Vamos começar com um exercício simples. Você possui algumas variáveis em Python que descrevem alguns dos seus atributos"

nome = "Ana"
idade = 25
cidade = "São Paulo"
"Com base nessas variáveis, gere uma apresentação curta de si mesmo, por exemplo:"

"Olá! Meu nome é Ana. Eu tenho 25 anos e moro em São Paulo."

apresentacao = (f"Olá! Meu nome é {nome}. Eu tennho {idade} anos e moro em {cidade}") #F é de função, necessario para executador uma função dentro da String
print(apresentacao)

#Neste exercício, utilizamos as f-strings do Python para inserir variáveis dentro da string 
#apresentacao de forma simples e prática. Em uma f-string, usamos chaves ( { } ) para indicar
#onde as variáveis serão inseridas. Neste caso, os trechos {nome}, {idade} e {cidade} 
#são substituídos pelos valores das respectivas variáveis.
#A variável apresentacao contém a string final, que exibimos na última linha do código.

##Seguimos agora para um exercício clássico de Python. Dada uma lista de números em Python: 

numeros = [10, 20, 30, 40, 50]
##Calcule a média dos valores dessa lista.

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média dos números é:", media)

#Explicação da solução
#Nesse código, temos uma lista de números chamada numeros. Para calcular a média, primeiro inicializamos 
#uma variável soma com o valor zero. Em seguida, percorremos cada número na lista numeros usando um for loop 
#for e adicionamos cada número à variável soma.
#Depois de percorrer todos os números, dividimos a soma pelo número total de elementos na lista numeros, 
#que obtemos através da função len(). Com essa operação, obtemos a média. Então, ao final do código, exibimos a média usando a função print().

#Exercício de Python 3: quem gastou mais dinheiro?
#Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, João e Pedro. 
#Cada valor na lista representa o gasto em uma das semanas do mês:

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

#Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro. Para isso, crie um código 
#em Python que responda a essa pergunta.

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")
    
#Explicação da solução
#Primeiro, somamos todos os gastos de João e Pedro usando a função sum(). Dessa forma, #
# são criadas as variáveis total_gastos_joao e total_gastos_pedro. Em seguida, comparamos os #
# totais de gastos usando uma estrutura condicional (if, elif, else) para determinar quem gastou mais #
# (ou se ambos gastaram a mesma quantidade). Por fim, o código exibe o resultado da comparação.

#Partindo de uma lista de palavras qualquer, como:

palavras = ["python", "asimov", "código", "web", "programação"]

#Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).

#Solução do exercício
palavras = ["python", "asimov", "código", "web", "programação"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print("A maior palavra é:", maior_palavra)
print("A menor palavra é:", menor_palavra)

#Nesse código, iniciamos as variáveis maior_palavra e menor_palavra com a primeira palavra da lista palavras. Em seguida, percorremos 
# a lista com um for loop. Para cada palavra, comparamos o comprimento dela (usando a função len()) com o comprimento das palavras 
# armazenadas em maior_palavra e menor_palavra.
#Se encontrarmos uma palavra com um comprimento maior que maior_palavra, atualizamos essa variável. Fazemos a mesma 
# operação com menor_palavra, atualizando a variável caso encontremos uma palavra de menor tamanho.
#Assim, garantimos que teremos encontrado a maior e a menor palavra da lista ao final da iteração. Por fim, exibimos 
# essas palavras com a função print().

##Exercício de Python 5: encontre o segundo maior valor
#Nesta atividade, você possui uma lista de números qualquer. Por exemplo:
numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros.sort()
segundo_maior = numeros[-2]

print("O segundo maior valor da lista é:", segundo_maior)

#Explicação da solução
#Nessa solução, utilizamos o método .sort() para ordenar a lista numeros em ordem crescente. Note que o método .sort() opera 
# diretamente sobre a lista, portanto não é preciso guardar nenhum resultado em uma variável.
#Uma vez feita essa ação, podemos encontrar o segundo maior elemento realizando uma indexação na lista. Como os valores 
# foram ordenados, o segundo maior valor corresponderá ao penúltimo elemento da lista, o qual acessamos pela indexação numeros[-2]. 
#Em seguida, basta exibi-lo para resolver o exercício

#Você fez uma pequena pesquisa de preferência entre três produtos A, B e C. Na entrevista, cada entrevistado precisava 
# escolher seu produto preferido. Os votos obtidos nessa pesquisa estão representados na lista abaixo:

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]
#Agora, seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, crie um dicionário onde a 
# chave é cada produto, e o valor é o número de votos que o produto recebeu.

contagem_votos = {} #Dicionario

for produto in votos:
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(contagem_votos)

#Explicação da solução
""" Para criar um dicionário com o número de votos para cada produto, podemos iterar pela lista de votos e contar quantas vezes
cada produto aparece.
No código acima, iniciamos um dicionário vazio chamado contagem_votos. Em seguida, iteramos sobre cada voto na lista votos e, 
para cada produto, verificamos se ele já está no dicionário contagem_votos. Se sim, incrementamos o valor associado a essa chave em 1. 
Caso contrário, criamos uma associação nova no dicionário, associando o produto e o valor de contagem 1 (já que ele está sendo contado 
pela primeira vez).
No final, o dicionário contagem_votos possuirá o número de votos para cada produto, o qual exibimos com a função print(). """

""" Exercício de Python 7: detector de palíndromos
Crie um script capaz de detectar palíndromos. Um palíndromo é uma palavra que permanece a mesma se for lida de trás para frente, 
como “arara” ou “radar”.
"""
palavra = "arara"

palavra_invertida = palavra[::-1]
eh_palindromo = palavra == palavra_invertida

if eh_palindromo:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
    
""" Explicação da solução
No código acima, partimos de uma palavra qualquer (variável palavra) e usamos a sintaxe de slicing de listas [::-1] para criar uma versão 
invertida da palavra (variável palavra_invertida). Em seguida, comparamos a palavra original com sua versão invertida usando o operador de 
igualdade == e atribuímos o resultado (um valor booleano) a uma variável eh_palindromo. Por fim, usamos uma estrutura condicional para verificar 
se a variável eh_palindromo possui o valor True ou False, exibindo uma mensagem adequada de acordo com o resultado. """

""" Exercício de Python 8: formate os números de venda
Você possui uma loja de computadores. No mês passado, suas vendas subiram significativamente. Então, você calculou a porcentagem de aumento
vendas e anotou o valor como um número (float) em Python: """


""" Formate o número em duas casas decimais, exibindo o seguinte texto: "O aumento percentual de vendas foi de 32.05%". """

aumento_vendas = 32.048701

aumento_formatado = "{:.2f}".format(aumento_vendas)
print(f"O aumento percentual de vendas foi de {aumento_formatado}%")

""" Explicação da solução
Nessa solução, usamos o método .format() de strings para formatar números em duas casas decimais. Para fazer isso, usamos o indicador 
de formatação :.2f. Note que essa formatação já faz o arredondamento do valor além da segunda casa decimal.
Em seguida, basta usar a função print() para exibir a mensagem desejada. Neste exemplo, utilizamos ainda um f-string para inserir a 
variável aumento_formatado ao texto da mensagem. """

""" Exercício de Python 9: detector de spam """
""" Você está recebendo muitos emails de spam na sua empresa. Para bloqueá-los, você deseja criar um script em Python capaz de detectar um email 
de spam a partir do seu domínio (o nome após o sinal de @).
Crie uma função em Python para implementar essa funcionalidade. A função deve exibir uma mensagem de acordo com o e-mail ser spam ou não. 
Para o exercício, considere que e-mails enviados do domínio @xyz.com são mensagens de spam.
"""

def detectar_spam(email):
    if email.endswith("@xyz.com"):
        print(f"O email de {email} é spam.")
    else:
        print(f"O email de {email} não é spam.")
        
        detectar_spam("usuario1@empresa.com")
# output:
# O email de usuario1@empresa.com não é spam.


detectar_spam("usuario2@xyz.com")
# output:
# O email de usuario2@xyz.com é spam.

""" Definimos uma função chamada detectar_spam(), que recebe um endereço de e-mail como argumento. Dentro da função, usamos o método de string 
.endswith() para verificar se o endereço de e-mail termina com o domínio "@xyz.com". Em seguida, com base no resultado dessa comparação, 
exibimos a mensagem avisando se o e-mail é de spam ou não. """

Exercício de Python 10: índices do alfabeto
Vamos para o último desafio: crie uma função que retorna uma letra do alfabeto, dado o seu índice. Por exemplo, o índice 1 deve retornar a letra "A", o índice 2 deve retornar a letra "B" e assim por diante. Caso o índice esteja acima ou abaixo dos limites do alfabeto, a função deve retornar um string vazio.

Solução do exercício
def indice_do_alfabeto(indice):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= indice <= 26:
        return alfabeto[indice - 1]
    else:
        return ''

print(indice_do_alfabeto(1))
# output: "A"

print(indice_do_alfabeto(3))
# output: "C"

print(indice_do_alfabeto(30))
# output: ""
Testar
Explicação da solução
Na função indice_do_alfabeto(), criamos uma string chamada alfabeto, que contém todas as letras maiúsculas do alfabeto. Dentro da função, verificamos se o índice está dentro do intervalo válido de 1 a 26. Se estiver, retornamos a letra correspondente ao índice fornecido usando indexação de strings (note que usamos indice - 1 nesta etapa porque a indexação em Python parte de zero). Por outro lado, se o índice estiver fora do intervalo válido, a função retorna uma string vazia.