class Person:

    def __init__(self, name, age): #creare nome e age come variabili oltre self obbligatorio 
        self.name = name
        self.age = age
    
    def printData(self):
        print(f"nome: {self.name},età: {self.age}") #creo funzione per stampare i dati immessi al di fuori della classe
    
    def changeName(self, newName):   #creo funzione per cambiare nome in caso si voglia
        self.name = newName
    
    def changeAge(self, newAge): #funzione per cambiare età
        self.age = newAge


class People:          #created a subclass to person that always takes init and self in order to connect to it and saves a list of people
    def __init__(self):
        self.people_list = []

    def addPerson(self, person):        #adding in subclass of person the person in a list
        self.people_list.append(person)

    def checkAges(self):
        min_age = float('inf')  
        min_person = None
        for person in self.people_list:
            if person.age < min_age:
                min_person = person.name
                min_age = person.age
        print(f"{min_person} è il nome di chi ha età inferiore: {min_age}") #check min age and name
            

    def printAllPeople(self):
        for person in self.people_list:   #to print all people in list
            person.printData()

# Create some people
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
john = Person("John Doe", 15) #created before adding

# Create a group of people
group = People()
group.addPerson(alice)
group.addPerson(bob)
group.addPerson(john)
group.addPerson(Person("Fji", 198)) #create while adding

# Check ages inside the class
group.checkAges()

# Print all people
group.printAllPeople()