import random
import Modulo_reutilizavel_lista

#Classe de Carta

def baralho(n):
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valores = Modulo_reutilizavel_lista.mult_list(8, valores)
    num_cartas = 0
    baralho = Modulo_reutilizavel_lista.criar_lista()

    # Adiciona 104 cartas viradas para cima
    for valor in valores:
        num_cartas+=1
        carta = {'valor': valor, 'Face_Up': n}
        Modulo_reutilizavel_lista.adicionar_elemento(baralho, carta)
        #baralho.append(carta)

    #print(num_cartas)

    if n == 0:
        return embaralhar(baralho)
    else:
        return baralho



def embaralhar(baralho):
    random.shuffle(baralho)
    return baralho

def mudaVal(n):
    if n == 'J':
        n = 11
    if n == 'Q':
        n = 12
    if n == 'K':
        n = 13
    if n == 'A':
        n = 1
    return int(n)

def sucessor(n1, n2):
    val1 = mudaVal(n1['valor'])
    val2 = mudaVal(n2['valor'])


    return val1 == val2 + 1




    
