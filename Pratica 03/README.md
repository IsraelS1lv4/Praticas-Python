PRÁTICA 03
Arquivos TXT em Python

EXERCÍCIO 1: Para realizar os exercícios práticos adiante, utilize o seu ambiente Python preferido, e digite os seguintes códigos:

Criando arquivos TXT
```
    nome_do_arquivo = input('Nome do arquivo a ser criado:')
    arquivo = open(nome_do_arquivo, 'w+')
    texto = arquivo.readlines()
    texto.append(input('Insira o texto:'))
    arquivo = open(nome_do_arquivo, 'w')
    arquivo.writelines(texto)
    arquivo.close()
```
A partir desse momento, usando um editor de textos, crie um arquivo denominado arquivo.txt e adicione algumas linhas de texto aleatório. Certifique-se de que o arquivo está na mesma pasta de onde o seu código Python está executando, senão dará erro.

Iterar sobre um arquivo
```
    arquivo = open('arquivo.txt', 'r')
    for linha in arquivo:
    print(linha)
    arquivo.close()
```
Ler todas as linhas em uma única string
```
    arquivo = open('arquivo.txt', 'r')
    unica_string = arquivo.read()
    arquivo.close()
```
Ler todas as linhas em uma lista
```
    arquivo = open('arquivo.txt', 'r')
    lista = arquivo.readlines() # readlinesssssss
    arquivo.close()
```
Ler linha a linha do arquivo
```
    arquivo = open('arquivo.txt', 'r')
    primeira_linha = arquivo.readline()
    segunda_linha = arquivo.readline()
    terceira_linha = arquivo.readline()
    # etc...
    arquivo.close()
```
Criar um arquivo vazio<br>
Certifique-se de que o arquivo não exista, se não ele irá apagar seu conteúdo.
```
    arquivo = open('novo-arquivo.txt', 'w')
    arquivo.close()
```
Apagar o conteúdo de um arquivo
```
    arquivo = open('novo-arquivo.txt', 'w')
    arquivo.close()
```
Escrever em um arquivo<br>
Se o arquivo já existir ele irá sobrescrever todo o conteúdo.
```
    arquivo = open('novo-arquivo.txt', 'w')
    arquivo.write('nova linha')
    arquivo.close()
```

EXERCÍCIO 2:
Crie um programa que solicita ao usuário um número para ser calculado o seu fatorial [pode usar math.factorial(n)]. Em seguida, salve o resultado em um arquivo, conforme o exemplo a seguir:
```
O fatorial de 5 é 120
```
A cada execução do programa, a informação anterior do arquivo não deve ser apagada, apenas são adicionadas novas linhas, conforme exemplo adiante:
```
O fatorial de 5 é 120
O fatorial de 7 é 5040
```
