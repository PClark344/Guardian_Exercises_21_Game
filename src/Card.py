import constant

class card:
	
	def __init__(self,suit,face):
		self.suit = suit
		self.face = face
		
	def get_card(self):
		return self.suit, self.face
		
	def set_card(self):
		self.suit = suit
		self.face = face
		
	def get_card_value(self):
		if self.face in constant.CARD_NON_PICTURES:
			self.value = self.face
			return self.value
		elif self.face in constant.CARD_PICTURES_NOT_ACE:
			self.value = 10
			return self.value
		elif self.face == constant.CARD_ACE:
			self.value = 11
			return self.value
		else:
			return constant.CARD_VALUE_NOT_FOUND_ERROR
		
