'''9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.'''

class User:

    def __init__(self,name:str,last_name:str,*attributes:str):
        self.name = name
        self.last_name = last_name
        self.attributes = attributes

    def describe_user(self):
        print(f"name: {self.name}, last name: {self.last_name}")
        for attribute in self.attributes:
            print(attribute)
        
    def greet_user(self):
        print(f"Hello user {self.name}!")

    
user1 = User("Jacopo","Sfolgori","alto 180cm","occhialuto")
user2 = User("Federico","Rotella","numero 1","che pro")
user3 = User("Riccardo","Leonori","fai il rangoli","maledetto")

User.describe_user(user1)
User.describe_user(user2)
User.describe_user(user3)

User.greet_user(user1)
