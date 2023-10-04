from Deck import *
from Tabuleiro import *



def inicia_jogo(baralho):

    #Cria 10 colunas
    colunas = [[] for coluna in range(10)]

    #Distribui 4 primeiras colunas com 6 cartas
    for coluna in colunas[:4]:
        coluna.extend(baralho.pop() for _ in range(6))

    #Distribui 6 colunas com 5 cartas
    for coluna in colunas[4:]:
        coluna.extend(baralho.pop() for _ in range(5))

    #Vira a ultima carta para cima
    for coluna in colunas:
        if coluna:
            coluna[-1]['Face_Up'] = True

    
    print("Instruções:")
    print("Para mover cartas de uma coluna para outra digite mover")
    print("Caso queira pegar cartas do monte digite monte")

    #Imprime a mesa
    imprime_tabuleiro(colunas)
    return colunas



#Define as condicionais de cada jogada
def jogadas(x, baralho, colunas):
    if x == 'monte':
        if baralho == None:
            print("Monte não tem mais cartas\n")
            return
        else:
            monte(colunas, baralho)
            
    if x == "mover":
        colunaAtual = int(input("Qual coluna você deseja mexer?\n"))
        carta = input("A partir de qual carta você deseja pegar?\n")
        proximaColuna = int(input("Para qual coluna você deseja mover?\n"))
        mov_cartas(colunaAtual, carta, proximaColuna, colunas)

    imprime_tabuleiro(colunas)
        

#Ve se a coluna que recebeu cartas pode receber essas cartas
#Verifica se a carta de cima é antecessora da debaixo
#Retorna bool
def mov_check(colunaA, cartas, pColuna):
    reais = ["J","Q","K"]
    
    if(pColuna[-1] in reais and cartas[0] in reais):
        vAtribuidoPColuna = reais.index(pColuna[-1])+11
        vAtribuidoCartas = reais.index(cartas[0])+11
        if(vAtribuidoPColuna>vAtribuidoCartas):
            return True
        
    elif(pColuna[-1] in reais and cartas[0] not in reais):
        return True
    
    elif(pColuna[-1] not in reais and cartas[0] not in reais):
        if(pColuna[-1] == 'A' or cartas[0] == 'A'):
            if (cartas[0] == 'A' and pColuna[-1] != 'A'):
                return True
            else:
                return False
                
        elif(int(pColuna[-1]) > int(cartas[0])):
            return True
    
    else:
        return False


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