from random import randint

# the dice class that will display the roll and determine whether the player
# rolled doubles or not
class Dice:
    def __init__(self):
        self.dye_1 = 1
        self.dye_2 = 1
        self.doubles = False

    def roll(self):
        self.dye_1 = randint(1, 6)
        self.dye_2 = randint(1, 6)

        print(f"You rolled a {self.dye_1} and {self.dye_2}. Move {self.dye_1 + self.dye_2} spaces.\n")
            
    def is_doubles(self):
        if self.dye_1 == self.dye_2:
            self.doubles = True
            return self.doubles
        self.doubles = False
        return self.doubles