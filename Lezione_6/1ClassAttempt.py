class Person:

    def __init__(self, name, age): #creare nome e age come variabili oltre self forzato
        self.name = name
        self.age = age
    
    def printData(self):
        print(f"nome: {self.name}\netà: {self.age}") #creo funzione per stampare i dati immessi al di fuori della classe
    
    def changeName(self, newName):   #creo funzione per cambiare nome in caso si voglia
        self.name = newName
    
    def changeAge(self, newAge): #funzione per cambiare età
        self.age = newAge


alice = Person("Alice W.", 45)      #aggiungo dati alla classe
bob = Person("Bob M.", 36)

alice.changeName("Armanda")     #sfrutto il cambio nome


if alice.age > bob.age: #controllo età invocando le funzioni annesse alla classe
    alice.printData()
else:
    bob.printData()


people:list = [alice, bob, Person(input("inserisci nome: "),int(input("inserisci età: "))), Person("Ricky",4), Person("Sylas",88)] #creo lista anche con input per 5 persone 

people[-1].age = 50     #modifico ultimo in lista età 
people[-1].printData()  #stampo ultimo in lista, questo in generale per invocare una variable che sia creata in input o con la funzione all'interno della lista basta l'indice della lista per invocarlo

min = Person("minimo",float("inf"))
for person in people:
    if person.age < min.age:        #loop check per controllo età minima
        min.changeAge(person.age) #cambio età con funzione per il minimo (OVVIAMENTE POTREI FARE UNA FUNZIONE PER ENTRAMBI MA E' PER ESEMPIO QUESTO)
        min.changeName(person.name) #cambio nome con funzione per il minimo

min.printData()
