'''6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.'''

person: dict = {"name" : "Federico", "last_name" : "Puzzone", "age" : 54, "city" : "Rome"}

for key, value in person.items():
    print(key, value)