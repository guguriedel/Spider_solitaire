from Deck import *
from Tabuleiro import *

def imprime_tabuleiro(colunas):
    for i, coluna in enumerate(colunas, start=1):
        print(f"Coluna {i}: {[str(card) for card in coluna]}")

def inicia_jogo(deck):
    #Cria as colunas e distribui as cartas
    colunas = deck.mesa(face_up=False)

    #Vira a ultima carta para cima
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
    return colunas


#Define as condicionais de cada jogada
def jogadas(x, deck, colunas):
    if x == 'm':
        if deck.monte_null():
            print("Monte não tem mais cartas\n")
            return
        else:
            deck.monte(colunas)
    imprime_tabuleiro(colunas)

#Ve se a coluna que recebeu cartas pode receber essas cartas
#Verifica se a carta de cima é antecessora da debaixo
#Retorna bool
def mov_check():
    return

#Confere se a carta pode ser movimentada
#Ou seja, se não há cartas fora de ordem debaixo dela
def retira_check():
    return

#Verifica se a coluna que recebeu cartas tem 14 cartas ordenadas de K até A
def completa_check():
    return

#Função que verifica se o jogador ganhou
def vitoria_check():
    return