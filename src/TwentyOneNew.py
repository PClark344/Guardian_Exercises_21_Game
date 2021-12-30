#################################################################
# AUTHOR:  PAUL DAVID CLARK
# PROGRAM: Twenty One Game from GitHub site for Guardian Tests
# DATE:    22 December 2021
# VERSION: 1.0
#################################################################

### import required modules #####################

from os import path
from sys import exit
import constant
import random


suits = constant.SUIT_TYPES
faces = constant.CARD_FACES
unshuffled_cards = []
shuffled_cards = []		
		
for suit in suits:
	for face in faces:
		card = suit + face
		unshuffled_cards.append(card)
		
#print('unshuffled cards = ',unshuffled_cards)

random.shuffle(unshuffled_cards)
shuffled_cards = unshuffled_cards

#print('shuffled cards = ',shuffled_cards)



