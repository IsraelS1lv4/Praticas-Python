#def main():
#    a = int(input("Digite o primeiro numero: "))
#    b = int(input("Digite o segundo numero: "))
#    soma = a + b
#    print("A soma de", a, "+", b, "eh igual a", soma)
#main()

#def main():
#    num = int(input("Digite um inteiro: "))
#    soma = 0
#    while num != 0:
#        soma = soma + num
#        num = int(input("Digite um inteiro: "))
#    print("A soma eh", soma)
#----------------------------------------------
#main()

def main():
    metros = float(input("Digite a quantidade de metros: "))
    milimetros = metros*1000
    print(metros, "metros corresponde a", milimetros, "milimetros ")
main()

def main():
    x = int(input("Digite a quantidade de segundos: "))
    dias = int(x/86400)
    horas = int((x/3600)-(dias*24))
    minutos = int((x/60)-(horas*60)-(dias*1440))
    segundos = x-((dias*86400)+(horas*3600)+(minutos*60))
    print(x,"segundos = ", dias, "dia(s), ", horas, "hora(s), ", minutos, "minuto(s) e ", segundos,"segundo(s)")
main()


