class Animal():
    #Parenteses nao sao obrigatorios caso nao tenha argumentos!!!

    #init --> construtor
    def __init__(self):
        print("Animal criado")

    def imprimir(self):
        print("Este é um animal")

    def comer(self):
        print("Hora de comer")

    def emitir_som(self):
        pass


#Herança
class Cachorro(Animal):

    def __init__(self):
        #iniciando construtor da super classe
        Animal.__init__(self)
        print("Cachorro criado")

    #sobscrever metodo
    def emitir_som(self):
        print("au au")

class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Gato criado")

    def emitir_som(self):
        print("miau")


rex = Cachorro()
zeze = Gato()

rex.emitir_som()
zeze.emitir_som()
rex.imprimir()
zeze.imprimir()