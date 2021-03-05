#Read in classes
import os
os.chdir('/Users/ksharma/Documents/ML Engineer/Software Engineering/Python/Object Oriented Programming/OOP Projects/Card Game/')


from WarClasses import Card, Deck, Player, War


#Create deck of cards and shuffle
deck1= Deck()
deck1.shuffle()

#Create our war players
player1= Player('Jill', 15_000)
player2= Player('Jack', 15_000)

#Each player places bets
player1.place_bet(5_000)
player2.place_bet(5_000)

#Each player draws a card
player1.card= deck1.draw_card()
player2.card= deck1.draw_card()
player1.card.show()

#Play War
round1= War(player1, player2)
round1.player1.card.show()