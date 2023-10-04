from Partida import *



baralho = baralho()
colunas = inicia_jogo(baralho)


while True:
   x = input("Insira sua jogada:\n")
   jogadas(x, baralho, colunas)