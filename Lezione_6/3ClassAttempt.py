class Student:
    
    StudentGrades = [] #creates a list for all grades to be added

    StudentCount = 0 #creates a variable that counts students created
    
    def __init__(self,name,studyProgram,grade,**kwargs):
        self.name = name 
        self.studyProgram = studyProgram
        self.grade = grade
        
        Student.StudentGrades.append(grade) #add grade to list

        for key, value in kwargs.items(): #check how many to convert attributes
            setattr(self, key, value) #gives attributes related to the **kwargs you want to add inside setattr and ofc it is mandatory to make it work to be setting the 1st attribute as self
        
        Student.StudentCount += 1 # update value of the student after it is created

    def printInfo(self):
        
        print(f"nome: {self.name} \nstudy program: {self.studyProgram} \ngrade: {self.grade}")
        
        for key, value in self.__dict__.items(): # creates a dict
            if key not in ['name', 'studyProgram','grade']:  #Exclude already printed attributes
                print(f"{key.capitalize()}: {value}") #capitalize the first letter or number in key and print Key: value
    
    @classmethod #VITAL WAY IN ORDER TO MAKE THE FUNCTION WORK WITH ALL CLS INFOS OTHERWISE LIKE EXPLAIN IN SLIDE IS JUST POOPOO
    def getaverage(cls):
        if cls.StudentCount == 0:
            print("nessun voto")
            return #nothing to be printed so it wont do anything in case
        avg = sum(cls.StudentGrades) / cls.StudentCount         # checking by calling cls.grade and count since they work outside objects and inside class 
        print(f"{avg} è il voto medio fra gli studenti inserito") 

    
class groupstudents: #created a underclass with a list of students

    def __init__(self):
        self.group_list = [] #list added here
    
    def addPerson(self, person):        
        self.group_list.append(person) #append inside list the student

    def printAllPeople(self):
        for person in self.group_list:   #print all students in list
            person.printInfo()


group:list = groupstudents() #creates a list with the subclass of students list

group.addPerson(Student("F","Coglionologia",14,gender="it", age=6)) #add a person to group list with student function

group.printAllPeople() #print every student in list


alice = Student("Alice","boh",29) #add a student to be counted but outside the list 
print(Student.StudentCount) #print the counter of students

Student.getaverage() #again since it is a class based function and not object in class function it will be called from the classname.functionnameoutsideobjects() 