'''Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''
import math
user_input = float(input("Enter a number to find its square root: "))
user_input2 = float(input("Enter a second number to find its square root: "))
a = float(user_input)
b = float(user_input2)

if a > b:
    result = math.sqrt(a**2 - b**2)
    print(f"The square root of n1 {a}**2 - n2 {b}**2 is: {result}")
else:
    if b > a:
        print("errore")

user_input = float(input("Enter a number to find its square root: "))
user_input2 = float(input("Enter a second number to find its square root: "))
a = float(user_input)
b = float(user_input2)

if a > b:
    result = (a**2 - b**2) ** 0.5  
    print(f"The square root of n1 {a}**2 - n2 {b}**2 is: {result}")
else:
    if b > a:
        print("errore")