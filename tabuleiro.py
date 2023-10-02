from Deck import *
from Partida import *

def imprime_tabuleiro(colunas):
    for i, coluna in enumerate(colunas, start=1):
        print(f"Coluna {i}: {[str(card) for card in coluna]}")

#Função que move as cartas de uma coluna para outra
def mov_cartas( colunaAtual, carta, proximaColuna, colunas):
    
    print(colunas[colunaAtual-1])
    print(colunas[colunaAtual-1][-1])
    print(type(colunas[colunaAtual-1][-1]))
    
    index = colunas[colunaAtual-1].index(carta)
    print(index)
    
    cartasMovidas = colunas[colunaAtual-1][index:]
    print(cartasMovidas)
    
    movcheck = mov_check(colunaAtual, cartasMovidas, proximaColuna)
    if movcheck == True:
        colunas[colunaAtual].append(cartasMovidas)
        for el in cartasMovidas:
            colunas[colunaAtual-1].remove(el)
    else:
        print("Não foi possível fazer essa movimentação\n")
    
    return
#Função que move as coluna para o topo
def coluna_completa():
    return

