import unittest
from line_bot import Line_Bot

class Test_Left_Right(unittest.TestCase):
    def setUp(self):
        self.line_bot = Line_Bot()
    
    def test_left_right(self):
        done = raw_input("Please place robot with the line on its right(type DONE when complete")
        assert self.line_bot.get_orientation() == 'right'
        
        done = raw_input("Please place robot with the line on its left(type DONE when complete")
        assert self.line_bot.get_orientation() == 'left'
    
    def tearDown(self):
        pass
    
if (__name__ == "__main__"):
    unittest.main()

