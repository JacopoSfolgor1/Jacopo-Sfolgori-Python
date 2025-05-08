'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''

numbers : list = [i for i in range(1,30+1)]

print(f"{numbers[0:3]}")
print(f"{numbers[len(numbers) // 2 - 2: len(numbers) // 2 + 1 ]}")
print(f"{numbers[len(numbers) - 3 : len(numbers)]}")