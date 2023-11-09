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
def mov_cartas( colunaAtual, carta_origem, proximaColuna, colunas):
    indices = [i for i, carta in enumerate(colunas[colunaAtual]) if carta['Face_Up'] and carta['valor'] == carta_origem]

    if not indices:
        print('Carta n encontrada')
        return
    carta_index = indices[-1]

    cartas_movidas = colunas[colunaAtual][carta_index:]
    colunas[proximaColuna].extend(cartas_movidas)
    colunas[colunaAtual] = colunas[colunaAtual][:carta_index]

    if colunas[colunaAtual]:
        colunas[colunaAtual][-1]['Face_Up'] = True

    return

#Função que move as coluna para o topo
def coluna_completa():
    return

