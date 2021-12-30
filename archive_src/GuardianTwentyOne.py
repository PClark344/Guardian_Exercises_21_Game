#################################################################
# AUTHOR:  PAUL DAVID CLARK
# PROGRAM: Twenty One Game from GitHub site for Guardian Tests
# DATE:    23 August 2021
# VERSION: 1.0
#################################################################

### import required modules #####################

import random
 
### Initialise Variables

names = ['Sam','Dealer']
suits = ['H','D','S','C']
faces = ['2','3','4','5','6','7','8','9','J','Q','K','A']
faces_vals = [2,3,4,5,6,7,8,9,10,10,10,11]
unshuffled_cards = []
shuffled_cards = []
sam_total = 0
dealer_total = 0
card_val = 0

### Function to produce a deck of cards ##########

def produce_deck():
	for suit in suits:
		for face in faces:
			card = suit + face
			unshuffled_cards.append(card)
	
	return unshuffled_cards


### shuffle cards using built in fn ############## 

def shuffle_deck():

	random.shuffle(unshuffled_cards)
	shuffled_cards = unshuffled_cards

	return shuffled_cards

### Function to deal cards ###################### 

def deal_card():

	global card_val
	card_val = 0
	
	card = unshuffled_cards.pop(0)
	suit = card[0]
	face = str(card[1])


	
	val_pos = 0
	for test_face in faces:
		if face == test_face:
			card_val = faces_vals[val_pos]
			exit
		else:
			val_pos = val_pos + 1

	print('Name = ',name)
	print('Card = ',card)
	print('Card Value = ',card_val)
	
	return card_val

### Function to check winner ######################
			
def check_winner(sam_total,dealer_total):
	
	if sam_total < 17 or sam_total == 17:
		pass
	elif sam_total > 21:
		print('Bust - dealer wins')
	elif sam_total == 21: 
		print('sam is the winner')
	elif sam_total > dealer_total:
# add code here to determine when sam will win
		pass
	elif dealer_total > 21:
		('Bust - Sam wins')
	else:
		print('dealer is the winner')
	
	return
	
	
### invoke code to produce deck of cards ##########

produce_deck()
print('unshuffled cards = ',unshuffled_cards)
shuffle_deck()
print('shuffled cards = ',unshuffled_cards)

### Initial 2 card deal ###########################

sam_total = 0
dealer_total = 0
card_val = 0

for name in names:
	for card_count in range(0,2):
		deal_card()

		if name == 'Sam':
			sam_total = sam_total + card_val
		else:
			dealer_total = dealer_total + card_val
			
	print('Sam total = ',sam_total)
	print('Dealer total = ',dealer_total)
	
	check_winner(sam_total,dealer_total)
	

#### sams deals ############

##### dealers deals ########


		

		

