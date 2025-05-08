'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, 
include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. '''

pet1: dict = {"name": "Star Destroyer", "owner's name" : "Federico", "kind of animal" : "hamster"}
pet2: dict = {"name": "Samba", "owner's name" : "Jacopo", "kind of animal" : "capybara"}
pet3: dict = {"name": "Sssenor", "owner's name" : "Riccardo", "kind of animal" : "snake"}
list_pets: list = [pet1, pet2, pet3]

for pet in list_pets:
    for key, value in pet.items():
        print(key, value)