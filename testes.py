import Partida
import Tabuleiro
import Deck

#Teste mov_check

valores = ['A', '2', '3', '4', '5', '6', '8', '9', '10', 'J', 'Q', 'K']
baralho = []

for valor in valores:
        carta = {'valor': valor, 'Face_Up': False}
        baralho.append(carta)

print(Partida.completa_check(baralho))