import random

#Classe de Carta

def baralho():
    valores = 8 * ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    num_cartas = 0
    baralho = []

    # Adiciona 104 cartas viradas para cima
    for valor in valores:
        num_cartas+=1
        carta = {'valor': valor, 'Face_Up': False}
        baralho.append(carta)

    print(num_cartas)
    return embaralhar(baralho)



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




    
