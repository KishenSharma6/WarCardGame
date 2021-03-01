#Read in classes
import os
os.chdir('/Users/ksharma/Documents/Data Science/Software Engineering/Object Oriented Programming/OOP Projects/Card Game/')


from WarClasses import Card, Deck, Player


deck1= Deck()
deck1.draw_card().show()
deck1.shuffle()
deck1.show()
deck1.draw_card(deck1)

deck1.cards[0]
player1= Player('Jane', 3000)
player2= Player('Joe', 5000)
player1.place_bet(2000)
player2.place_bet(2000)
deck1.draw_card().show()
player1.card= deck1.draw_card()
player2.card= deck1.draw_card()
player1.card.show()
player2.card.show()
player1.a
# player2= Player('Bob', 4000)
# player2.draw(deck1)
# player2.card
deck1.draw_card()