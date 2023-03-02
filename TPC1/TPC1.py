import unicodedata
import string

#1- Programa que pergunta ao utilizador o nome e imprime em maiúsculas.

def maiusculas():
    maiuscula= input("Qual é o teu nome? ")
    return maiuscula.upper()

#2- Função que recebe array de números e imprime números pares

def pares():
    x = input("Lista: ")
    z=[]
    y= x.split()
    i= [x for x in y if int(x) % 2==0]
    for x in i:
        z.append(int(x))
    return z

#3 - Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa

def ler_inverso():
    x = input("Nome do ficheiro ou o seu path: ")
    file= open(x,encoding="UTF-8")
    l=file.readlines()
    return(l[::-1])

#4 - Função que recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro

def ocorrenciasfreq():
    x = input("Nome do ficheiro ou o seu path: ")
    file= open(x,encoding="UTF-8")
    ler= file.read()
    ler=ler.lower()
    for pontuacao in ".,:;!?()[]{}":
        ler = ler.replace(pontuacao,"")
    palavras=ler.split()
    contador= {}
    for palavra in palavras:
        if palavra not in contador:
            contador[palavra] = 1
        else:
            contador[palavra] += 1
    ordenados = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    top= {}
    for i in range(10):
        palavr,contagem = ordenados[i]
        top[palavr]= contagem
    return(top)

#5 - Função que recebe um texto como argumento e o ”limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc

def limpa_texto():
    texto=input("Texto para limpar: ")
    for punctuation in string.punctuation:
        texto = texto.replace(punctuation, f" {punctuation} ")
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = " ".join(texto.split())
    return texto

#6 - Given a string “s”, reverse it

def inverter():
    palavra= input("Palavra dada: ")
    return palavra[::-1]

#7 - Given a string “s”, returns how many “a” and “A” characters are present in it

def contador_a_A():
    palavra = input("Palavra dada: ")
    return palavra.count('a') + palavra.count('A')

#8 - Given a string “s”, returns the number of vowels there are present in it

def contador_vogais():
    palavra = input("Palavra dada: ")
    vogais = 'aeiouAEIOU'
    return sum(1 for v in palavra if v in vogais)

#9 - Given a string “s”, convert it into lowercase

def porminisculo():
    palavra = input("Palavra dada: ")
    return palavra.lower()

#10 - Given a string “s”, convert it into uppercase

def pormaiusculo():
    palavra = input("Palavra dada: ")
    return palavra.upper()

def menu():
    exercicio= input("Qual o número do exercício: ")
    if (exercicio == "1"):
        print(maiusculas())
    elif (exercicio =="2"):
        print(pares())
    elif (exercicio == "3"):
        print(ler_inverso())
    elif (exercicio == "4"):
        print(ocorrenciasfreq())
    elif (exercicio == "5"):
        print(limpa_texto())
    elif (exercicio == "6"):
        print(inverter())
    elif (exercicio == "7"):
        print(contador_a_A())
    elif (exercicio == "8"):
        print(contador_vogais())
    elif (exercicio == "9"):
        print(porminisculo())
    elif (exercicio == "10"):
        print(pormaiusculo())

menu()
