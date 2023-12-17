arq2 = open('E:/LEARNING/DSA Python/6 - Tratamento de arquivos, modulos, pacotes e funções built-in/arquivo1.txt', 'w')

arq2.write(" Dota 2 é excelente")
arq2.close()

arq3 = open('E:/LEARNING/DSA Python/6 - Tratamento de arquivos, modulos, pacotes e funções built-in/arquivo1.txt', 'r')
print(arq3.read())
arq3.close()


## Parte 3


##Funcao filter

lista = [0,1,2,3,4,5,6,7,8,9,10]

def verificaPar(num):
    if num % 2 == 0:
        return True

list(filter(verificaPar, lista))
print(list(filter(verificaPar, lista)))