'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.'''
import time
numbers : list = [i for i in range(20+1)]
for n in numbers:
    time.sleep(1)
    print(n)

i: int = 1 

while i < 21:
    print(i)
    i += 1