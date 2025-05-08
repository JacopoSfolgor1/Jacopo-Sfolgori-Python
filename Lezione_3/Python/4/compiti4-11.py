'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, 
and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.'''


pizzas : list = ["diavola", "tartufo", "margherita"]

friend_pizzas = pizzas.copy()
print(friend_pizzas)

pizzas.insert(1, "crostino")
friend_pizzas.insert(2, "bufala")

for pizza in pizzas:     
    print(f"my favourite pizzas are {pizza}")
for pizza in friend_pizzas:     
    print(f"my friend's favorite pizza {pizza}")
    
i = 0
i2 = 0
while i < len(pizzas):
    print(f"my favourite pizzas are {pizzas[i]}")
    i += 1 
while i2 < len(friend_pizzas):
    print(f"my friend's favorite pizza {friend_pizzas[i2]}")
    i2 += 1
    