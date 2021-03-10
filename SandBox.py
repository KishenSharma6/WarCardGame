#Read in classes
import os
import importlib
os.chdir('/Users/ksharma/Documents/ML Engineer/Software Engineering/Python/Object Oriented Programming/OOP Projects/Card Game/')

from WarClasses import Card, Deck, Hand
import WarClasses
importlib.reload(WarClasses)

#Create deck of cards and shuffle
deck1= Deck()
deck1.shuffle()
deck2= Deck()

hand1= Hand()
hand1.draw_card(deck1)
