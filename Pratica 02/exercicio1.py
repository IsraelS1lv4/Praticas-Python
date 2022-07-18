from math import radians
from math import pow
from math import tan
from math import exp

def main():
    a = int(input("Digite um numero 'a': "))
    b = int(input("Digite um numero 'b': "))
    print("a =",a,"\nb =",b)
    print("pow(a,b) =", pow(a,b))
    print("tan(a) =", tan(radians(a)))
    print("exp(b) =",exp(b))
main()