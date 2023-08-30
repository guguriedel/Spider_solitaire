from tabuleiro import *
from regras import *

#Cria o deck
deck = Deck()

#Cria as colunas e distribui as cartas
colunas = deck.mesa(face_up=False)

for coluna in colunas:
    if coluna:
        coluna[-1].face_up = True


#Imprime as Instruções
print("Instruções:")
print("Para mover cartas de uma coluna para outra digite o numero da coluna e depois o numero da carta")
print("por fim digite o numero da coluna destino")
print("Caso queira pegar cartas do monte digite 'm'")

#Imprime a mesa
imprime_tabuleiro(colunas)

#Inicia o switch
x = 0
'''
Aqui está o modelo do Switch que será usado no jogo
while x != 'Fim':
    print("Insira a sua jogada desejada:")
    
    x = input()
    if (x == 'm'):
        deck.monte(colunas)
    if(check_x()):
'''

deck.monte(colunas)
imprime_tabuleiro(colunas)
