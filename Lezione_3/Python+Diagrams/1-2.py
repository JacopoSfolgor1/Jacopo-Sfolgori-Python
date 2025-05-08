'''Trova il massimo tra 4 numeri:

Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''

#WHILE

i:int = 1
max: float = float(input("primo inserisci numero: "))

while i < 4:
    n:float = float(input("inserisci numero: "))
    if max < n:
        max = n
    i += 1

print(f"{max} è il numero massimo")



#FOR

max: float = float(input("primo inserisci numero: "))

for i in range(3):
    n:float = float(input("inserisci numero: "))
    if max < n:
         max = n

print(f"{max} è il massimo")



#REPEAT

max:float = float(input("primo inserisci numero: "))
i:int = 1

while True:
    n:float = float(input("inserisci numero: "))
    if max < n:
        max = n
    i += 1 
    if i == 4:
        break

print(f"è il massimo: {max}")