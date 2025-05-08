'''Exercise 4 (Folder 9 ex_4.py)
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu'''

class Food:
    
    def __init__(self,name,price,description):
        self.name = name
        self.price = price
        self.description = description
        

class Menu:
    
    def __init__(self,menu_list = None):
        if menu_list is None:
            self.menu_list = []
        else:
            self.menu_list = menu_list

    def addFood(self,food):
        self.menu_list.append(food)
        

    def removeFood(self,food):
        self.menu_list.remove(food)
        
    def printPrices(self):
        for food in self.menu_list:
            print(f"name: {food.name}, price: {food.price}$, description: {food.description}")

    def AveragePrice(self):
        if len(self.menu_list) == 0:
            return 0 
        total_price = sum(food.price for food in self.menu_list)
        return total_price / len(self.menu_list)
    

carbonara = Food("carbonara", 14, "bonissima ao")

pizza = Food("Pizza Tartufo", 18, "la migliore senza scuse")

lasagna = Food("Lasagna classica", 12, "non ti puoi mai sbagliare ordinandola")

menu = Menu()

menu.addFood(carbonara)
menu.addFood(pizza)
menu.addFood(lasagna)

menu.printPrices()

average_price = menu.AveragePrice()
print(f"{average_price:.2f}$ is average menu price")