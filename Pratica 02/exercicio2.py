from pessoas import Pessoa
def main():
    obj1 = Pessoa("Joao", 1)
    obj2 = Pessoa("Maria", 0)
    print("Nome 'obj1':", obj1.nome)
    print("Sexo 'obj1':", obj1.sexo)
    print("Nome 'obj2':", obj2.nome)
    print("Sexo 'obj2':", obj2.sexo)
main()

from pessoas import Pais
def main():
    obj1 = Pais("Francisco", 1, "Arthur")
    obj2 = Pais("Juliana", 0, "Antonia")
    print("Nome 'obj1':", obj1.nome)
    print("Sexo 'obj1':", obj1.sexo)
    print("Nome da criança 'obj1':", obj1.getCrianca())
    print("Nome 'obj2':", obj2.nome)
    print("Sexo 'obj2':", obj2.sexo)
    print("Nome da criança 'obj2':", obj2.getCrianca())
main()
