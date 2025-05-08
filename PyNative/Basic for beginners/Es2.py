'''Exercise 2: Print the Sum of a Current Number and a Previous number
Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.'''

list_n: list = []

i = 0

while i < 10:
    number: int = int(input("Inserisci un numero: "))
    list_n.append(number)
    i += 1
    

for n in list_n:
    sum: int = n + (n-1)
    print(f"{sum} è somma di {n} e {n-1}")