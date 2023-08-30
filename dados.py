import random

#Classe de Carta

class Card:
    def __init__(self, valor, face_up = False):
        self.valor = valor
        self.face_up = face_up

    def __str__(self):
        return f"{self.rank}"
    
    #from card import Card

    class Deck:
        def __init__(self):
            self.valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            self.cards = [Card(valor) for valor in self.valores]
            self.shuffle()

        def shuffle(self):
            random.shuffle(self.cards)

print("Hello Wolrd")

