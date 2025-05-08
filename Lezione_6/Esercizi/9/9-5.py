'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.'''

class User:

    def __init__(self,name:str,last_name:str,login_attempts:int = 0,*attributes:str):
        self.name = name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.attributes = attributes

    def describe_user(self):
        print(f"name: {self.name}, last name: {self.last_name}, login attempts: {self.login_attempts}")
        for attribute in self.attributes:
            print(attribute)
        
    def greet_user(self):
        print(f"Hello user {self.name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        self.login_attempts = 0
        
    

user1 = User("Jacopo","Sfolgori",2,"alto 180cm","occhialuto")

print(f"starting login attempts: {user1.login_attempts}, by user {user1.name}")

User.increment_login_attempts(user1)
print(f"{user1.login_attempts} incrementing login attempts by 1")

User.increment_login_attempts(user1)
print(f"{user1.login_attempts} incrementing login attempts by 1")

User.increment_login_attempts(user1)
print(f"{user1.login_attempts} incrementing login attempts by 1")

User.increment_login_attempts(user1)
print(f"{user1.login_attempts} incrementing login attempts by 1")

User.increment_login_attempts(user1)
print(f"{user1.login_attempts} incrementing login attempts by 1")

User.reset_login_attempts(user1)
print(f"reset the count of login attempts: {user1.login_attempts}")
