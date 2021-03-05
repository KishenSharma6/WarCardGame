import random

class Card():
    def __init__(self, suit, value):
        self.suit= suit
        self.value= value

    def show(self):
        print("%s of %s" %(self.value, self.suit))

class Deck():
    #test
    def __init__(self):
        self.cards= []
        self.build()
        
    def build(self):
        #Build Deck of cards using Card Class
        for suit in ['diamonds', 'clubs', 'hearts', 'spades']:
            for value in range(1,14):
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        for i in range(len(self.cards) - 1,0,-1):
            r= random.randint(0,i)
            self.cards[i], self.cards[r]= self.cards[r], self.cards[i] 

    def draw_card(self):
        return self.cards.pop()

class Player():
    def __init__(self, name, amount, card= None):
        self.name= name
        self.amount= amount
        self.card= card

    def show(self):
        """
        Show card
        """
        for card in self.cards:
            card.show()

    def place_bet(self, wager):
        if wager > self.amount:
            print('%s does not have enough funds to place bet' %(self.name))
        else:
            self.wager= wager
            self.amount= self.amount - wager

class War():
    def __init__(self, player1, player2):
        self.player1= player1
        self.player2= player2
    
    def play_game(self):
        pass
    
