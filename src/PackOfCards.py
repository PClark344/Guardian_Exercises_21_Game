### import required modules #####################

import random
import constant
import Card

class packofcards:
	
	def __init__(self):
		self.suits = constant.SUIT_TYPES
		self.faces = constant.CARD_FACES
		self.cards = []
		
	def produce_deck(self):
		for suit in self.suits:
			for face in self.faces:
				card = suit + face
				self.cards.append(card)
	
		return self.cards

	def shuffle_deck(self):
		random.shuffle(self.cards)

		return self.cards
		
	def deal_card(self):
		top_card = pop(self.cards(0))
		top_card_suit = top_card[0,1]
		top_card_face = top_card[1,-1]
		dealt_card = Card.card(top_card_suit,top_card_face)
		
		return dealt_card

