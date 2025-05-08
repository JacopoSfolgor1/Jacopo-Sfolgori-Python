'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.'''

cities: dict = {"Kyoto" : {"population": "2.55 millions", "country" : "Japan", "fact" : "has the best ramen"}, 
                "Rome" : {"population": "2.76 millions", "country" : "Italy", "fact" : "has the best carbonara"},
                "Svalbard" : {"population": "2500", "country" : "Norway", "fact" : "best place to have some peaceful cold"}}

for key, value in cities.items():
    print(f"\n{key} infos are: ")
    for key1, value1 in value.items():
        print(f"{key1}: {value1} ")