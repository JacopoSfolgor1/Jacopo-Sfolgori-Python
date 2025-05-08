'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

class Restaurant: 
    
    def __init__(self,name:str,cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"name: {self.name}, cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The restaurant {self.name} is open!")


restaurant = Restaurant("DAJE TUTTA","Italian, trattoria romana")

print(restaurant.name)
print(restaurant.cuisine_type)

Restaurant.describe_restaurant(restaurant)

Restaurant.open_restaurant(restaurant)