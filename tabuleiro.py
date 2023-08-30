import random

#Classe de Carta

class Card:
    def __init__(self, valor, face_up = False):
        self.valor = valor
        self.face_up = face_up

    def __str__(self):
        return f"{self.valor}"
    

class Deck:
    def __init__(self, num_decks=1):
        self.valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(valor) for valor in self.valores]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        
    def mesa(self):
        #Colunas é como se fosse a mesa
        colunas = []

        #Como nosso objetivo é distribuir 6 cartas para 4 colunas, iremos fazer 2 for
        for elem in range(4):
            #Cria 1 coluna
            coluna = []
            for elem in range(6):
                #Distribui 6 cartas
                if self.cards:
                    card = self.cards.pop()
                    coluna.append(card)
            colunas.append(coluna)

        #Distribui 5 cartas para 6 colunas
        for elem in range(6):
            #Cria 1 coluna
            coluna = []
            for elem in range(5):
                #Distribui 6 cartas
                if self.cards:
                    card = self.cards.pop()
                    coluna.append(card)
            colunas.append(coluna)

        return colunas
        
    

    def monte(self, colunas):
        for coluna in colunas:
            if self.cards:
                #Removo a carta adicionada para não haver repetições
                card = self.cards.pop()
                coluna.append(card)