'''9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win
'''

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

    def simulate_until_win(self, my_ticket = None):
        if my_ticket == None:
            my_ticket = self.draw_ticket()
        tries = 0
        while True:
            drawn = self.draw_ticket()
            if drawn == my_ticket:
                return tries, drawn
            tries += 1

lottery = LotteryMachine()
my_ticket = lottery.draw_ticket()
tries, winning_ticket = lottery.simulate_until_win(my_ticket)

print("Your ticket:", *my_ticket)
print("The winning ticket:", *winning_ticket)
print("How many attempts it took to win:", tries)
