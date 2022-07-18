AULA PRÁTICA: 01
Introdução a Python

Para realizar os exercícios práticos adiante, utilize a linguagem Python.
PARTE 1 – Usando o Idle
Digite no prompt do Idle os seguintes comandos:
>>>2+4+1
Em seguida, digite:
>>> a=7
>>> b=4 # isto é um comentário
>>> a=a+b
Consulte o valor da variável ‘a’ simplesmente digitando a e pressione Enter.
Em seguida, digite:
>>> 21 == 3*7+1
Em seguida, digite:
>>> x = [1,3,7,14]
>>> x
>>> y = ['a', 'b', 'c']
>>> lista1 = x
>>> lista2 = [lista1,y]
>>> min(x)
>>> sum(x)
>>> x.append(20)

PARTE 2 – Usando o Sublime
Exemplo 1: soma de dois números:
def main():
    a = input("Digite o primeiro numero: ")
    b = input("Digite o segundo numero: ")
    soma = a + b
    print("A soma de", a, "+", b, "eh igual a", soma)
main()
Para executar, abra o command do Windows e digite PATH = C:/Python27/ e em seguida digite
python c:\caminho_para_seu_arquivo.py

Exemplo 2: Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma. Por exemplo, para a sequência 12 17 4 -6 8 0, o seu programa deve escrever o número 35. Segue abaixo trecho do código.

def main():
    num = int(input("Digite um inteiro: "))
    soma = 0
    while num != 0:
    soma = soma + num
    num = int(input("Digite um inteiro: "))
    print("A soma eh", soma)
#----------------------------------------------
main()

Exercícios:
1) Escreva um programa que leia um valor em metros e o exiba convertido em
milímetros.
2) Faça um programa para converter segundos em dias, horas, minutos e segundos. Por
exemplo: 200 000 segundos = 2 dias, 7 horas, 33 minutos e 20 segundos