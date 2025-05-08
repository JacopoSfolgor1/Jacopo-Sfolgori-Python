class Room:
    def __init__(self, id = None, floor = None, seats = None, area = None):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = self.seats * 2
        
    def get_id(self):
        return self.id
        
    def get_floor(self):
        return self.floor
        
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area

class Building:
    def __init__(self,name = None, address = None, floors = None, rooms = None):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = rooms if rooms is not None else []
        
    def get_floors(self):
        return self.floors
        
    def get_rooms(self):
        return self.rooms
        
    def add_room(self, room):
        if self.floors[0] <= room.get_floor() and room.get_floor() <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)
    
    def area(self):
        return sum(room.get_area() for room in self.rooms)


class Person:
    def __init__(self, cf = None, name = None, surname = None, age = None): 
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
    
class Student(Person):
    def __init__(self, cf = None, name = None, surname = None, age = None):
        super().__init__(cf, name, surname, age)
        self.group = None
        
    
    def set_group(self, group):
        self.group = group
        
class Lecturer(Person):
    def __init__(self, cf = None, name = None, surname = None, age = None):
        super().__init__(cf, name, surname, age)
    
class Group:
    def __init__(self, name = None, limit = None, students = None,lecturers = None):
        self.name = name
        self.limit = limit
        self.students = students if students is not None else []
        self.lecturers = lecturers if lecturers is not None else []
        
    
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        limit_lecturers = max(1, len(self.students) // 10)
        return limit_lecturers
        
    def add_student(self,student):
        if len(self.students) < self.limit:
            self.students.append(student)
    
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.limit:
            self.lecturers.append(lecturer)
            
class Course:
    def __init__(self, name = None, groups = None):
        self.name = name
        self.groups = groups if groups is not None else []
    
    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                return

    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)


 	

# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")


'''
EXPECTED OUTPUT
### SMI ###
Stanze nell'edificio SMI: ['123', '333', '111']
Area totale dell'edificio SMI: 212 m²
### ARMELLINI ###
Stanze nell'edificio ITIS: ['567', '888', '999']
Area totale dell'edificio ITIS: 152 m²
### COURSE DETAILS ###
Studenti nel gruppo Fullstack: ['1234']
Studenti nel gruppo Cloud: ['5678', '9101', '2345', '6789', '1011', '3456', '7890', '1112', '4567', '8901']
Studenti nel gruppo Cyber: ['1123', '5678']'''