'''1- Safe Square Root: Write a function safe_sqrt(number) 
that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.'''
import math

def safe_sqrt(number:float = float(input("inserisci n: "))):
    
    if number < 0:
        raise ValueError("numero negativo")
    else:
        print(math.sqrt(number))

safe_sqrt()
    
