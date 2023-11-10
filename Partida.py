import Deck
import Tabuleiro



def inicia_jogo():
    baralho = Deck.baralho()

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
    Tabuleiro.imprime_tabuleiro(colunas)
    return baralho, colunas



#Define as condicionais de cada jogada
def jogadas(x, baralho, colunas):
    if x == 'para':
        print("O jogo foi interrompido\nObrigado por jogar\n\n")
        exit(1)
    if x == 'monte' or x == '+':
        if not baralho:
            print("Monte não tem mais cartas")
            return
        else:
            Tabuleiro.monte(colunas, baralho)
            
    if x == "mover": #or int(x) in range(0,9): - digitar coluna direto
        colunaAtual = int(input("Qual coluna você deseja mexer?\n"))
        carta = input("A partir de qual carta você deseja pegar?\n")
        proximaColuna = int(input("Para qual coluna você deseja mover?\n"))
        mov_check(colunaAtual, carta, proximaColuna, colunas)

    Tabuleiro.imprime_tabuleiro(colunas)
        

#Ve se a coluna que recebeu cartas pode receber essas cartas
#Verifica se a carta de cima é antecessora da debaixo
#Retorna bool
def mov_check(colunaAtual, cartas_origem, proximaColuna, colunas):
    #Verifica se minha coluna existe
    if (colunaAtual < 0 or colunaAtual >= 10) or (proximaColuna < 0 or proximaColuna >= 10):
        print("Colunas Inválidas.")
        return
    
    #Verifica se a coluna tem cartas
    elif not colunas[colunaAtual]:
        print("Coluna de Origem Vazia")
        return
    
    #conferir se a coluna contém a carta
    index_carta = -1
    for i, carta in enumerate(colunas[colunaAtual]):
        if carta['Face_Up'] and carta['valor'] == cartas_origem:
            index_carta = i
            break
    if index_carta == -1:
        print('Carta não encontrada na coluna ', colunaAtual)
        return
    
    #Cartas formam sequência
    for i in range(index_carta, len(colunas[colunaAtual]) - 1):
        if not Deck.sucessor(colunas[colunaAtual][i], colunas[colunaAtual][i+1]):
            print("As cartas selecionadas não formam uma sequência")
            return
        
    #Se a coluna que recebe as cartas está vázia, podemos mover qualquer carta 
    if not colunas[proximaColuna]:
        Tabuleiro.mov_cartas(colunaAtual, cartas_origem, proximaColuna, colunas)
        return

        
    #Conferir se a coluna recebe a carta sucessora ao ultimo valor da coluna
    elif not Deck.sucessor(colunas[proximaColuna][-1], colunas[colunaAtual][index_carta]):
        print("A carta não forma sequência com a última carta da coluna destino")
        return
    
    else:
        Tabuleiro.mov_cartas(colunaAtual, cartas_origem, proximaColuna, colunas)
        
    return


#Confere se a carta pode ser movimentada
#Ou seja, se não há cartas fora de ordem debaixo dela

def retira_check():
    return

#Verifica se a coluna que recebeu cartas tem 14 cartas ordenadas de K até A
def completa_check(coluna):
    if not coluna:
        return False

    valores_validos = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    # Filtra apenas as cartas viradas para cima
    cartas_viradas_para_cima = [carta for carta in coluna if carta['Face_Up']]

    # Verifica se as cartas viradas para cima estão em ordem decrescente de K até A
    for i, carta in enumerate(cartas_viradas_para_cima):
        if carta['valor'] != valores_validos[i]:
            return False

    return True

#Função que verifica se o jogador ganhou
def vitoria_check():
    return