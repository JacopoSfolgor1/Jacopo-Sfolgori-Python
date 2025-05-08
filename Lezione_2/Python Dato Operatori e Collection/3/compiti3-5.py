'''3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() 
call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

guest_list : list = ["Cesare", "Cleopatra", "Seneca"]
print(f"{guest_list} in this list {guest_list[2]} can't make it to dinner")
guest_list.remove(guest_list[2])
guest_list.append("Leonardo Da Vinci")
print(f"{guest_list[0]} Dine with me king \n{guest_list[1]} you are invited to dinner \n{guest_list[2]} would come to dinner?")