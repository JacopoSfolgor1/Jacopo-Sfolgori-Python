'''Exercise 3 (Folder 9 ex_3.py)
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''
class Animal:
    
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    

    def changeLegs(self, new_legs):
        self.legs = new_legs

    def setLegs(self, new_legs):
        self.legs = new_legs
    
    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(f"name: {self.name}, legs: {self.legs}")
    

dog = Animal("Dog",3)
bird = Animal("Bird",2)

print(f"{dog.name} name animal 1, {bird.name} name animal 2")

dog.legs = 3
print(f"{dog.name} has now {dog.legs} legs")

bird.setLegs(3)
print(f"legs of {bird.name} are now {bird.legs}")


print(f"{dog.getLegs()} legs {dog.name}, {bird.getLegs()} legs {bird.name}")

dog.printInfo()
bird.printInfo()


    