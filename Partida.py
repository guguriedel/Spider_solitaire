import Deck
import Tabuleiro



def inicia_jogo(n):
    baralho = Deck.baralho(n)

    #Cria 10 colunas
    colunas = [[] for coluna in range(10)]

    #Distribui 4 primeiras colunas com 6 cartas
    for coluna in colunas[:4]:
        #Não podemos usar o modulo de lista pois estamos falando do ultimo elem 
        #e nao de um elem especifico
        coluna.extend(baralho.pop() for _ in range(6))

    #Distribui 6 colunas com 5 cartas
    for coluna in colunas[4:]:
        coluna.extend(baralho.pop() for _ in range(5))

    #Vira a ultima carta para cima
    for coluna in colunas:
        if coluna:
            coluna[-1]['Face_Up'] = True

    
    print("Instruções:")
    print("Para mover cartas de uma coluna para outra digite mover ou o numero da coluna que deseja mover.")
    print("Caso queira pegar cartas do monte digite monte ou '+'")
    x = input("Aperte 'Enter' para iniciar o jogo.")

    #Imprime a mesa
    Tabuleiro.imprime_tabuleiro(colunas)
    return baralho, colunas, 0



#Define as condicionais de cada jogada
def jogadas(x, baralho, colunas, cont):
    #Caso queira parar o jogo
    if x == 'para':
        print("O jogo foi interrompido\nObrigado por jogar\n\n")
        exit(1)

    #Pegar cartas do monte
    elif x == 'monte' or x == '+':
        #Baralho sem cartas
        if not baralho:
            print("Monte não tem mais cartas")
            return cont
        else:
            #Bota uma carta do monte em cada coluna
            Tabuleiro.monte(colunas, baralho)
            #Checa se em alguma das 10 colunas temos uma sequencia de K-A
            for i in range(0,9):
               if completa_check(colunas[i]):
                   cont = Tabuleiro.coluna_completa(i, colunas, cont)

    #Chama função para mover de uma coluna para outra        
    elif x == "mover" or x == 'move':
        colunaAtual = ver_int(input("Qual coluna você deseja mexer?\n"))
        carta = input("A partir de qual carta você deseja pegar?\n").upper()
        proximaColuna = ver_int(input("Para qual coluna você deseja mover?\n"))

        if mov_check(colunaAtual, carta, proximaColuna, colunas):
            #Se a coluna está completa - move ela pro cont
            if completa_check(colunas[proximaColuna]):
                cont = Tabuleiro.coluna_completa(proximaColuna, colunas, cont)


    #Exclui a necessidade de digitar o comando mover, basta digitar a col inicial
    elif ver_int(x) in range(0,10):
        colunaAtual = ver_int(x)
        carta = input("A partir de qual carta você deseja pegar?\n").upper()
        proximaColuna = ver_int(input("Para qual coluna você deseja mover?\n"))
        
        if mov_check(colunaAtual, carta, proximaColuna, colunas):
            #Se a coluna está completa - move ela pro cont
            if completa_check(colunas[proximaColuna]):
                cont = Tabuleiro.coluna_completa(proximaColuna, colunas, cont)

    else:
        print('Comando não reconhecido')

#Verifica se todas colunas estão com a ultima carta
#virada para cima
    for coluna in colunas:
        if coluna:
            if coluna[-1]['Face_Up'] == False:
                coluna[-1]['Face_Up'] = True
                
    Tabuleiro.imprime_tabuleiro(colunas)
    return cont


#Ve se a coluna que recebeu cartas pode receber essas cartas
#Ja executa a movimentação
#Para maior coesão a função poderia ter sido dividida em outras funções
def mov_check(colunaAtual, cartas_origem, proximaColuna, colunas):
    #Identifica se alguma das entradas é nula
    if not colunaAtual and colunaAtual != 0:
        print("Preencha todos os campos para realizar o movimento.")
        return False
    if not cartas_origem and cartas_origem != 0:
        print("Preencha todos os campos para realizar o movimento.")
        return False
    if not proximaColuna and proximaColuna != 0:
        print("Preencha todos os campos para realizar o movimento.")
        return False

    #Mapeia ocorrencias da carta na coluna
    indices = [i for i, carta in enumerate(colunas[colunaAtual]) if carta['Face_Up'] and carta['valor'] == cartas_origem]

    #Verifica se coluna existe
    if (colunaAtual < 0 or colunaAtual >= 10):
        print("Colunas Inválidas.")
        return False
    elif (proximaColuna < 0 or proximaColuna >= 10):
        print("Colunas Inválidas.")
        return False
     
    #Verifica se a coluna tem cartas
    elif not colunas[colunaAtual]:
        print("Coluna de Origem Vazia")
        return False
    

    #Pega a última ocorrência se houverem cartas
    elif indices:
        index_carta = indices[-1]
    else:
        print("Carta %s não encontrada." %cartas_origem)
        return False
    
    #Cartas formam sequência?
    for i in range(index_carta, len(colunas[colunaAtual]) - 1):
        if not Deck.sucessor(colunas[colunaAtual][i], colunas[colunaAtual][i+1]):
            print("As cartas selecionadas não formam uma sequência")
            return False
        
    #Se a coluna que recebe as cartas está vázia, podemos mover qualquer carta 
    if not colunas[proximaColuna]:
        Tabuleiro.mov_cartas(colunaAtual, cartas_origem, proximaColuna, colunas)
        return False

        
    #Conferir se a coluna recebe a carta sucessora ao ultimo valor da coluna
    elif not Deck.sucessor(colunas[proximaColuna][-1], colunas[colunaAtual][index_carta]):
        print("A carta não forma sequência com a última carta da coluna destino")
        return False
    
    else:
        #Todas condições foram atendidas. Pode mover!
        Tabuleiro.mov_cartas(colunaAtual, cartas_origem, proximaColuna, colunas)
        return True



#Verifica se a coluna que recebeu cartas tem 14 cartas ordenadas de K a

def completa_check(coluna):
    #Não precisamos de um caso coluna vazia pois essa função
    #Só é chamada ao receber cartas (Hipotese)

    valores_validos = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    # Filtra apenas as cartas viradas para cima
    cartas_viradas_para_cima = [carta['valor'] for carta in coluna if carta['Face_Up']]

      # Percorre a lista de valores do baralho
    for i in range(len(cartas_viradas_para_cima) - len(valores_validos) + 1):
        # Verifica se a subsequência do baralho é igual à sequência desejada
        if cartas_viradas_para_cima[i:i+len(valores_validos)] == valores_validos:
            return True
    # Se a sequência não for encontrada, retorna False
    return False



#Função que verifica se o jogador ganhou
def vitoria_check(cont):
    if cont == 8:
        print('Você Venceu!!!!')
        return True
    else:
        return False
    

def ver_int(x):
    try:
        return int(x)
    except ValueError:
        print("Entrada não preenchida corretamente!")
        return None