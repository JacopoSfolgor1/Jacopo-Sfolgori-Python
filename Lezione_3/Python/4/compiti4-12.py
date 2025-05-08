    
'''4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space.
Choose a version of foods.py, and write two for loops to print each list of foods.'''


foods_1 : list = ["pizza", "fries", "rice"]
foods_2 : list = ["hamburger", "truffle", "mushrooms"]

for food in foods_1: 
    print(food)
    
for food in foods_2:
    print(food)

i = 0 
i2 = 0
while i < len(foods_1):
    print(f" list 1 {foods_1[i]}")
    i += 1
while i2 < len(foods_2):
    print(f" list 2 {foods_2[i2]}")
    i2 += 1
    