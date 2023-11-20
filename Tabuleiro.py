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
    #Mapeia ocorrencias da carta na coluna
    indices = [i for i, carta in enumerate(colunas[colunaAtual]) if carta['Face_Up'] and carta['valor'] == carta_origem]

    #Pega a última ocorrência
    carta_index = indices[-1]

    cartas_movidas = colunas[colunaAtual][carta_index:]
    colunas[proximaColuna].extend(cartas_movidas)
    colunas[colunaAtual] = colunas[colunaAtual][:carta_index]

    #Tendo cartas na coluna que perdeu cartas, virá essa carta pra cima
    if colunas[colunaAtual]:
        colunas[colunaAtual][-1]['Face_Up'] = True

    return

#Função que move a coluna para o topo
def coluna_completa(coluna_index, colunas, cont):
    sequencia = []
    
    #Encontra a Sequência
    for carta in colunas[coluna_index][::-1]:
        sequencia.insert(0, carta)
        if carta['valor'] == '':
            break
    print(f"Sequência encontrada: {[carta['valor'] for carta in sequencia]}")
    
    for carta in sequencia:
        colunas[coluna_index].remove(carta)
    
    print("Coluna após remoção da sequência:")
    for carta in colunas[coluna_index]:
        print(carta['valor'], end=' ')
    print()
    
    return cont+1



