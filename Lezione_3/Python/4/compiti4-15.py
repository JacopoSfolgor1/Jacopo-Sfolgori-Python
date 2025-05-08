'''4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.'''

number : list = [i**3 for i in range(1,10+1)]
for n in number:
    print(n)
    
foods_1 : list = ["pizza", "fries", "rice"]
foods_2 : list = ["hamburger", "truffle", "mushrooms"]

for food in foods_1: 
    print(food)
    
for food in foods_2:
    print(food)

numbers : list = [i for i in range(1,30+1)]

print(f"{numbers[0:3]}")
print(f"{numbers[len(numbers) // 2 - 2: len(numbers) // 2 + 1 ]}")
print(f"{numbers[len(numbers) - 3 : len(numbers)]}")