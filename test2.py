from CP_Project import *
import unittest
from unittest.mock import patch
from io import StringIO

class TestAdventureGame(unittest.TestCase):
    
    def setUp(self):
        # Set up a fresh player for each test case
        self.player = chara_trait(100, 10)

    @patch('CP_Project.input', create=True)
    @patch('sys.stdout', new_callable=StringIO)
    def test_successful_gameplay1(self, mock_stdout, mock_input):
        # Add enough inputs to ensure the game completes or reaches a terminal point
        mock_input.side_effect = ['north', 'grab rope', 'head back',  'west', 'throw rope', 'sail home']

        # Run the function, capturing printed output
        player_spawn(self.player)

        # Retrieve printed output from the mock_stdout
        output = mock_stdout.getvalue()

        self.assertIn("You are the Master of Game.", output, "test pass")
        
    @patch('CP_Project.input', create=True)
    @patch('sys.stdout', new_callable=StringIO)
    def test_successful_gameplay2(self, mock_stdout, mock_input):
        # Add enough inputs to ensure the game completes or reaches a terminal point
        mock_input.side_effect = ['north', 'enter house', 'grab map','head back','go to valley','go da way']

        # Run the function, capturing printed output
        player_spawn(self.player)

        # Retrieve printed output from the mock_stdout
        output = mock_stdout.getvalue()

        self.assertIn("You are the Master of Game.", output, "test pass")
        
        

if __name__ == "__main__":
    unittest.main()
    
  
    


    
