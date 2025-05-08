'''Exercise 14: Print a downward half-pyramid pattern of stars

* * * * *  
* * * *  
* * *  
* *  
*'''

n: int = int(input("inserisci n: "))
while n > 0:
    n_str = '*' * n
    print(n_str)
    n -= 1