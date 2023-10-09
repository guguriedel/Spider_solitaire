import Partida


baralho, colunas = Partida.inicia_jogo()


while True:
   x = input("Insira sua jogada:\n")
   x = x.lower()

   
   Partida.jogadas(x, baralho, colunas)