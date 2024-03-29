import Partida
import Modulo_reutilizavel_lista
import Deck



def imprime_tabuleiro(colunas):
    for i, coluna in enumerate(colunas, 0):
        print(f'Coluna {i}: ', end=' ')

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
            Modulo_reutilizavel_lista.adicionar_elemento(coluna, carta)
            #coluna.append(carta)
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
    lista = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']


    #Cria uma sequencia modelos
    for valor in lista:
        carta = {'valor': valor, 'Face_Up': True}
        Modulo_reutilizavel_lista.adicionar_elemento(sequencia, carta)
        #sequencia.append(carta)
    
    #Remove essa sequencia modelo da lista
    for carta in sequencia:
        Modulo_reutilizavel_lista.remover_elemento(colunas[coluna_index], carta)
        #colunas[coluna_index].remove(carta)
    
    
    return cont+1



