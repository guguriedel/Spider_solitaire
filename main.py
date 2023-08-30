from tabuleiro import *


deck = Deck(num_decks = 2)

colunas = deck.mesa()

for i, colunas in enumerate(colunas, start=1):
    

deck.monte(colunas)