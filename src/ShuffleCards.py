### import required modules #####################

import random
import constant

class packofcards:
	
	def __init__(self):
		self.suits = constant.SUIT_TYPES
		self.faces = constant.CARD_FACES
		self.unshuffled_cards = []
		self.shuffled_cards = []		
		
	def produce_deck(self):
		for suit in suits:
			for face in faces:
				card = suit + face
				self.unshuffled_cards.append(card)
	
		return self.unshuffled_cards

	def shuffle_deck(self):

		self.shuffled_cards = random.shuffle(self.unshuffled_cards)
		print(self.shuffled_cards)

		return self.shuffled_cards

