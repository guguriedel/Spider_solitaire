from Partida import *


deck = Deck()
colunas = inicia_jogo(deck)

while True:
    x = input("Insira sua jogada:\n")
    jogadas(x, deck, colunas)