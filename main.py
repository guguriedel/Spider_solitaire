import Partida





baralho, colunas = Partida.inicia_jogo()


while True:
   x = input("Insira sua jogada:\n")
   Partida.jogadas(x, baralho, colunas)