'''9-11. Imported Admin: Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.'''

class user:

    def __init__(self, first_name: str, last_name: str, username: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"First name: {self.first_name}, last name: {self.last_name}, username: {self.username}, email: {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} AKA {self.username}!")
    


class Privileges:
    
    def __init__(self, privileges = None):
        self.privileges = privileges if privileges is not None else []

    def show_privileges(self):
        print(f"{self.privileges}")
    
class Admin(user):
    
    def __init__(self, user: user, privileges: Privileges):
        self.user = user
        self.privileges = privileges

    def describe_user(self):
        return self.user.describe_user()

    def greet_user(self):
        return self.user.greet_user()

    def show_privileges(self):
        return self.privileges.show_privileges()