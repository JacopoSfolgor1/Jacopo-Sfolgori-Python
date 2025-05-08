'''6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, 
and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.'''

person1: dict = {"name" : "Federico", "last_name" : "Puzzone", "age" : 54, "city" : "Rome"}
person2: dict = {"name" : "Riccardo", "last_name" : "Apex" , "age" : 10, "city" : "Rome"}
person3: dict = {"name" : "Jacopo", "last_name" : "Sfolgori", "age" : 26, "city" : "Rome"}
list_people: list = [person1, person2, person3]

for person in list_people:
    for key, value in person.items():
        print(key, value)
