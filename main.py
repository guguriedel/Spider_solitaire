import Partida


baralho, colunas, cont = Partida.inicia_jogo()


while True:
   x = input("Insira sua jogada:\n")
   x = x.lower()

   
   cont = Partida.jogadas(x, baralho, colunas, cont)
   print('Colunas Completas:', cont)
   if Partida.vitoria_check(cont):
      print('Você venceu!')
      break