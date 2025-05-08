'''9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.'''

import random

class LotteryMachine:
    
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, ticket=None):
        self.ticket = ticket if ticket is not None else [random.choice(self.alpha) for i in range(5)] + [random.randint(0, 99) for i in range(10)]

    def draw_ticket(self):
        choice = random.choice(['letters', 'numbers'])
        if choice == 'letters':
            return [random.choice(self.ticket[:5]) for i in range(4)]
        else:
            return [random.choice(self.ticket[5:]) for i in range(4)]
        
    def print_winners(self):
        winners = self.draw_ticket()
        print("The winning ticket:", *winners)

lottery = LotteryMachine()
lottery.print_winners()
