'''Write a function called sum that takes a positive integer number n as input and returns the sum of the numbers from 0 to n.
If the input number n is negative, display an error message and the function must return None.
To implement the sum function, you must exclusively use a while loop and the parameter n passed as input to the function.
It is allowed to declare only one variable inside the function to manage the sum.
Then, call the function sum for n = -5 and n = 5'''

def sum(n:int) -> int:
    
    if n < 0:
        print("error")
        return None
    
    else:
        sum_n:int = 0
        while n > 0:
            sum_n += n
            n -= 1
        return int(sum_n)


print(f"{sum(-5)} somma -5")

print(f"{sum(5)} somma 5")


'''Write a Python function called recursiveSum that, given an integer n as input, recursively calculates the sum of the numbers
from 0 to n.
If the input number n is negative, display an error message and the function must return None.
Then, call the function recursiveSum for n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
None
--------------------------------------------------
15'''

def recursivesum(n:int) -> int: 

    if n < 0:
        print("error")
        return None
    
    elif n == 0:
        return 0
    
    else:
        return int(n + recursivesum(n -1))

print(recursivesum(5))

print(recursivesum(-5))


