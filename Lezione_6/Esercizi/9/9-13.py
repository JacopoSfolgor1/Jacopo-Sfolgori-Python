'''9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Die:
    def __init__(self, sides: int = 6):
        self.sides = sides if sides >= 6 else 6 

    def roll_die(self):
        self.n = random.randint(1, self.sides)
        print(f"Rolled: {self.n}")



dice1 = Die(10)

dice2 = Die(20)

for i in range(10):
    dice1.roll_die()

for i in range(10):
    dice2.roll_die()