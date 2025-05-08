'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.
Expected Output:
Sum of integers from 1 to 10 is 55
Sum of integers from 20 to 37 is 513
Sum of integers from 35 to 49 is 630'''


'''# sum of integers from 1 to 10
sum:int = 0
for i in range(1, 11):
    sum += i
print("Sum from 1 to 10 is", sum)

# sum of integers from 20 to 37
sum:int = 0
for i in range(20, 38):
    sum += i
print("Sum from 20 to 37 is", sum)

# sum of integers from 35 to 49
sum:int = 0
for i in range(35, 50):
    sum += i
print("Sum from 35 to 49 is", sum)'''


#function is better to compute 
def sum(a:int, b:int):
    somma:int = 0
    for i in range(a, b+1):
        somma += i
    return somma

print(f"Sum from 1 to 10 is {sum(1, 10)}")

print(f"Sum from 20 to 37 is {sum(20, 37)}")

print(f"Sum from 35 to 49 is {sum(35, 49)}")

mysum = sum(1, 10) #if i wanna save result as variable


'''Functions/3: Exercise
Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.
After you defined it, call the function with some arguments!'''

def subtract(a:int, b:int) -> int: # -> return value how you wish to be int/float etc.
    result:int = a - b
    return result

print(f"{subtract(111,11)} è la sottrazione fra 111 e 11")



def hello() -> None: #non ha parametri dentro e ritorna solo hello
    print("Hello")
   




