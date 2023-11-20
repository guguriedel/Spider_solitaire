import Partida




baralho, colunas, cont = Partida.inicia_jogo()


while True:
   x = input("Insira sua jogada:\n")
   x = x.lower()

   
   cont = Partida.jogadas(x, baralho, colunas, cont)
   print('Colunas Completas:', cont)
   if Partida.vitoria_check(cont):
      print('\n')
      print("Ao se deparar com uma tartaruga em cima de um muro.")
      print("Tenha certeza de que alguém à colocou lá.")
      break