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

 
     
           
if __name__ == '__main__':
    unittest.main()
