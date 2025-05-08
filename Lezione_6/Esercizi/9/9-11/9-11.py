'''9-11. Imported Admin: Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.'''


from users import user, Privileges, Admin

user1 = user("F","Rot","puzF", "fpuzzz@boh.it")

privileges = Privileges(["rimuovi tutto","aggiungi tutto","banna tutti"])

admin1 = Admin(user1,privileges)

admin1.describe_user()

admin1.greet_user()

admin1.show_privileges()