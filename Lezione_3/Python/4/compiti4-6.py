'''4-6. Odd Numbers: 
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number'''


numbers : list = [i for i in range(1,20+1,2)]
for n in numbers:
    print(n)

i = 1
while i < 21:
    print(i)
    i += 2