'''3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.'''

names : list = ["Federico", "Riccardo", "Jacopo"]

print(f"{names[0]} \n{names[1]} \n{names[2]}")
for name in names: 
    print(f"\n{name}")