'''Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. 
Otherwise, return their sum.'''

a:int = int(input("inserisci il primo numero: "))

b:int = int(input("inserisci il secondo numero: "))

c:list = a * b

match c:
    case c if c <= 1000:
        print(f"{a * b} prodotto")

    case c if c > 1000:
        print(f"{a + b} somma")