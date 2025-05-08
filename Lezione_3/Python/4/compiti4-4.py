'''4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)'''


numbers : list = [i for i in range(1000000+1)]
for n in numbers: 
    print(n)
    
i:int = 1 
while i < 1000001:
    print(i)
    i += 1