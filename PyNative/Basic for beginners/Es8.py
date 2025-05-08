'''Exercise 8: Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

n:int = 1

for n in range(10):
    for n in range(n):
        print(n, end = " ")
    print('\n')

