import random

class Card():
    def __init__(self, suit, value):
        self.suit= suit
        self.value= value

    def __repr__(self):
        return "%s of %s" %(self.value, self.suit)

class Deck():
        
    def __init__(self):
        self.cards= []                        
        self.build()
       
    def build(self):
        #Build Deck of cards using Card Class
        for suit in ['diamonds', 'clubs', 'hearts', 'spades']:
            for value in ["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand():
    def __init__(self, opponent= False):
        self.opponent= opponent
        self.cards= []
        self.value = 0
    
    def draw_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value= 0
        has_ace= False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == 'A':
                    self.value+= 11
                else:
                    self.value+= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.opponent:
            print(self.cards[0])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())