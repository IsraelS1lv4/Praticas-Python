import math
n = input('Digite um numero: ')
fatorial = math.factorial(int(n))
arquivo = open('arquivo.txt', 'a')
arquivo.write('O fatorial de '+ n +' é '+ str(fatorial)+'\n')
arquivo.close()


