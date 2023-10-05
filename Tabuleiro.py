import Partida
import Deck



def imprime_tabuleiro(colunas):
    for i, coluna in enumerate(colunas, 0):
        print(f'Coluna {i}: ', end=' ')

        """for carta in coluna[:-1]:
            print('X' if not coluna[-1]['Face_Up'] else carta['valor'], end = ' ')
        print('X' if not coluna[-1]['Face_Up'] else coluna[-1]['valor'])"""

        for carta in coluna:

            if carta['Face_Up']:
                print(carta['valor'], end='  ')
            else:
                print('X ', end=' ')

        print()

def monte(colunas, baralho):
    for coluna in colunas:
        if baralho:
            carta = baralho.pop()
            coluna.append(carta)
            carta['Face_Up'] = True
        #else:
            #print('Baralho não tem mais cartas')

#Função que move as cartas de uma coluna para outra
def mov_cartas( colunaAtual, carta, proximaColuna, colunas):
    
    print(colunas[colunaAtual-1])
    print(colunas[colunaAtual-1][-1])
    print(type(colunas[colunaAtual-1][-1]))
    
    index = colunas[colunaAtual-1].index(carta)
    print(index)
    
    cartasMovidas = colunas[colunaAtual-1][index:]
    print(cartasMovidas)
    
    movcheck = Partida.mov_check(colunaAtual, cartasMovidas, proximaColuna)
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

