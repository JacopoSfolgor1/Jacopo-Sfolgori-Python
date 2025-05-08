'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant: 
    
    def __init__(self,name:str,cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"name: {self.name}, cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The restaurant {self.name} is open!")

rest1 = Restaurant("DAJE TUTTA","Italian, trattoria romana")
rest2 = Restaurant("Tatakae","Japanese, sushi bar")
rest3 = Restaurant("Pizza da Nando", "Italian, pizzeria")

Restaurant.describe_restaurant(rest1)

Restaurant.describe_restaurant(rest2)

Restaurant.describe_restaurant(rest3)