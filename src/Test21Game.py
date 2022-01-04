###################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    Test21Game.py
# 
# PROGRAM DETAILS: 
#
# DOCS:            As specified in: 
#                  https://github.com/ 
#
# PURPOSE:         To test the modules in the Program
#                  TwentyOneNew.py
#
# DATE:            22 December 2021 
# 
# VERSION:         1.0
#
#################################################################

import unittest
import Card
import PackOfCards
import constant

class TestData(unittest.TestCase):

### test output of card function #####################

    def test_card_get_card_value_returns_correct_result(self):

        # Arrange
        card1 = Card.card('D','K')
        card2 = Card.card('H',9)
        card3 = Card.card('S','A')

        # Act
        result1 = card1.get_card_value()
        result2 = card2.get_card_value()
        result3 = card3.get_card_value()
        
        # Assert
        self.assertEqual(10, result1)
        self.assertEqual(9, result2)
        self.assertEqual(11, result3)
        
    def test_pack_of_cards_produce_deck_retns_correct_num_of_cards(self):
        # Arrange
        pack1 = PackOfCards.packofcards()
        
        # Act
        result1 = len(pack1.produce_deck())
        
        # Assert
        self.assertEqual(52,result1)
        
    def test_pack_of_cards_shuffle_deck_retns_correct_num_of_cards(self):
        # Arrange
        pack1 = PackOfCards.packofcards()
        unshuffled_cards = pack1.produce_deck()
        
        # Act
        result1 = len(pack1.shuffle_deck())
        
        # Assert
        self.assertEqual(52,result1)
        print(pack1.shuffle_deck())
 
        
if __name__ == '__main__':
    unittest.main()
