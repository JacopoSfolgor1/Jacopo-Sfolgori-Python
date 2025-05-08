'''6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output.'''

person1: dict = {"name" : "Federico", "last_name" : "Puzzone", "age" : 54, "city" : "Rome"}
person1_newinfo: dict = {"fav game": "exploding kittens"}
person_totalinfo: list = [person1, person1_newinfo]

for info in person_totalinfo:
    for key, value in info.items(): 
        print(f"{key}: {value}")