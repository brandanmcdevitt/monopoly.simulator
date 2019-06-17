import unittest
from players import Players
from dice import Dice

class TestPlayers(unittest.TestCase):
    """test the Player class"""
    def setUp(self):
        self.player = Players("Mike", "Dog")

    def test_init(self):
        """ensure that the init method returns a name, token and balance"""
        self.assertEqual(self.player.name, "Mike")
        self.assertEqual(self.player.token, "Dog")
        self.assertEqual(self.player.balance, 1500)

    def test_get_balance(self):
        """test to make sure that a correct balance is returned"""
        self.assertEqual(isinstance(self.player.balance, int), True)
        self.assertEqual(self.player.balance, 1500)

    def test_add_money(self):
        """test to check if a players balance can be increased with a value"""
        pass_go = self.player.add_money(200)
        self.assertEqual(pass_go, 1700)
    
    def test_add_money_is_int(self):
        """check to see if a TypeError is raised if the argument is not an int"""
        with self.assertRaises(TypeError):
            self.player.add_money("200")

    def test_remove_money(self):
        """test to check if a players balance can be decreased with a value"""
        tax = self.player.remove_money(100)
        self.assertEqual(tax, 1400)

    def test_remove_money_is_int(self):
        """check to see if a TypeError is raised if the argument is not an int"""
        with self.assertRaises(TypeError):
            self.player.remove_money("100")


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
    
    def test_roll(self):
        """the total of the rolled dice should be no less than 2 and no greater than 12"""
        roll = self.dice.roll()
        self.assertTrue(roll >= 2 and roll <= 12)
    
    def test_doubles_rolled(self):
        """if each dye has the same roll, doubles has been rolled"""
        self.dice.dye_1 = 1
        self.dice.dye_2 = 1
        self.assertEqual(self.dice.is_doubles(), True)

    def test_doubles_not_rolled(self):
        """if each dye has a different roll, doubles has not been rolled"""
        self.dice.dye_1 = 1
        self.dice.dye_2 = 5
        self.assertEqual(self.dice.is_doubles(), False)

if __name__ == '__main__':
    unittest.main()