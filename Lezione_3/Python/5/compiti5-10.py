'''5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. 
If it has, print a message that the person will need to enter a new username. 
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)'''

current_users: list = ["scemo", "scem", "sce","sc", "s"]
new_users: list = ["sc", "s", "omecs", "mecs", "esc"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. You need a new username.")
    else:
        print(f"Username '{new_user}' is available.")
        

i = 0
while i < len(new_users):
    if new_users[i].lower() in current_users_lower:
        print(f"Username '{new_users[i]}' is already taken. You need a new username.")
           
    else:
        print(f"Username '{new_users[i]}' is available.")
    i += 1