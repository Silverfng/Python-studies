import random
from os import system, name


#clear screen for every execution
def limpa_tela():
        _ = system('cls')

def game():

    limpa_tela()
    print("\nBem vindo ao jogo da Forca!")
    print("\nAdivinhe a palavra abaixo: \n")

    #lista de palavras
    palavras = ['banana', 'abacaxi', 'morango', 'abacate', 'uva']

    #random word
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Numero de chances
    chances = 6

    #lista para letras erradas
    letras_erradas = []

    while chances > 0:

        #present
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Tentative
        tentativa = input("\nDigite uma letra: ").lower()

        #condition
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra.capitalize())
            break

    #Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra.capitalize())


if __name__ == "__main__":
    game()
    print("\nParabéns você está aprendendo programação em Python com a DSA.\n\n")