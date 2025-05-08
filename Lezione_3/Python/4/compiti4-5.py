'''4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.'''

numbers : list = [i for i in range(1,1000000+1)]
print(f"{min(numbers)}, {max(numbers)}, {sum(numbers)}")


for number in numbers: 
    if number <= 1000000:
        print(number)
i = 1
while i < 1000001:
    print(number)
    i += 1

print(min(numbers), max(numbers), sum(numbers))