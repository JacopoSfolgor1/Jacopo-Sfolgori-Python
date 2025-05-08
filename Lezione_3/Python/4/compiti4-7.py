'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.'''

numbers : list = [i for i in range(3,30+1,3)]
for n in numbers:
    print(n)

i = 1    
while i < 31:
    print(i)
    i += 3 