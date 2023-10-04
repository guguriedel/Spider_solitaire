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


    return embaralhar(baralho)



def embaralhar(baralho):
    random.shuffle(baralho)
    return baralho


    
