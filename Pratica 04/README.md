PRÁTICA 04
Arquivos em Python (cont.)

EXERCÍCIO 1: 
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
```
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125
```
Neste arquivo, o nome do usuário possui exatamente 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
```
ACME Inc. Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
```
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
Para realizar o exercício anterior, o trecho de código a seguir precisa ser completado:
```
def toMB(tamanhoEmBytes):
    tamanhoEmBytes = float(______________)
    return (float(tamanhoEmBytes/(1024*1024)))
 
def percentualPorUsuario(lista, total):
    percentual = (lista[3]/total)*100
    #percentual = "{0:.2f}".format(percentual)
    lista.insert((len(cadaUsuario)), ______________)

def espacoMedioOcupado(lista, total):
    media = 0
    elementos = len(lista)
    ______________= (total)/(elementos+1)
    #media = "{0:.2f}".format(media)
    return ______________
#MAIN
usuarios = []
posicao = 1
total = media = 0
with open ("usuarios.txt","r") as arquivo:
    valor = 0
    for linha in arquivo:
        usuarios.append(linha.split()) 
    for cadaUsuario in usuarios:
        cadaUsuario.insert(0,posicao)
        valor = toMB(float(cadaUsuario[2]))
        total += valor
        cadaUsuario.insert((len(cadaUsuario)),valor)
        posicao+=1
    for cadaUsuario in usuarios:
        percentualPorUsuario(cadaUsuario, total)
media = espacoMedioOcupado(cadaUsuario,total)
with open ("relatorio.txt","w") as arquivo:
    arquivo.write("ACME Inc. Uso do espaço em disco pelos usuários.\n")
    arquivo. ______________ ("--------------------------------------------------------------\n")
    arquivo.write("Nr.\tUsuário ______________ ______________ \n\n")
    for cadaUsuario in usuarios:
        percentagem="{0:.2f}".format(round(cadaUsuario[3],2))
        arquivo.write(str(cadaUsuario[0])+'\t'+"{:<15}".format(cadaUsuario[1])+'\t'+"{:<16}".format(percentagem)+'MB'+'\t'+"{0:.2f}".format(cadaUsuario[4])+'%'+'\n')
    arquivo. ______________ ('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
    ______________.______________ ('\n\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
        ______________.close()
with open ("relatorio.txt","r") as arquivo:
    print(arquivo.read())
```
