#Read in classes
import os
os.chdir('/Users/ksharma/Documents/ML Engineer/Software Engineering/Python/Object Oriented Programming/OOP Projects/Card Game/')


from WarClasses import Card, Deck, Player


#Create deck of cards and shuffle
deck1= Deck()
deck1.shuffle()

#Create our war players
player1= Player('Jill', 15_000)
player2= Player('Jack', 15_000)

#Each player draws a card
player1.card= deck1.draw_card()
player1.card.show()