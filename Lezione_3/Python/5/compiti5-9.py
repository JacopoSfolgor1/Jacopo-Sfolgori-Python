'''5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.'''

usernames : list = ["Admin", "Francesco", "Federico", "Riccardo", "Jacopo"]
if usernames == []:
    print("empty list, need users")

for i in range(len(usernames)): 
    usernames.pop()
if usernames == []:
    print("empty list, users needed")

i = 0 
while i < len(usernames):
    usernames.pop()
i += 1
if usernames == []:
    print("empty list, users needed")
