from Partida import *

#Transforma o numero passado em indice da coluna
def id_coluna(coluna, carta):
    num = 0
    for elem in coluna:
        if str(elem) == carta:
            return num
        num+=1


deck = Deck()
colunas = inicia_jogo(deck)

while True:
    x = input("Insira sua jogada:\n")
    jogadas(x, deck, colunas)