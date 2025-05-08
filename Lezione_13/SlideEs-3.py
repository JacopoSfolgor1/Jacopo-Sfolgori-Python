'''Write a function sumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as
input to the function.
To solve the exercise, it is mandatory to use a while loop, and it is assumed that the value of b is always greater than the
value of a. Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
Finally, it is allowed to declare only one variable, in addition to the function parameters, to store the sum.
Then, call the function sumInRange for a = 5, b = 10 and for a = 10, b = 5.
Expected Output:
45
-------
45'''


def sumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp 
    sum:int = 0
    
    while b >= a:
        sum +=  b
        b -= 1
    return int(sum)

print(sumInRange(a=10,b=5))

print(sumInRange(a=5,b=10))



#recursive method


def recsumrange(a:int,b:int)-> int:
    
    if a > b:
        
        temp:int = a
        a = b 
        b = temp
    
    if b == a:
        return int(a)

    else: 
        return int(b + recsumrange(a, b-1))
    

print(recsumrange(a=5,b=10))
print(recsumrange(a=10,b= 5))