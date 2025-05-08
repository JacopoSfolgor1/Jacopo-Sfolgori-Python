'''3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.'''

guest_list : list = ["Cesare", "Cleopatra", "Seneca"]
print(len(guest_list))

if not guest_list:
    print("empty list")

if guest_list:
    print("full list")

if len(guest_list): #if 0 wont print
    print("ciao")

if len(guest_list) > 0:
    print("full list")