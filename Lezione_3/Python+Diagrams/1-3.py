'''P3. Calcolo della somma di numeri positivi
Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente. 
Quindi, se un numero è negativo o zero, ignora quel valore nella somma.'''

sum: int = 0
cont: int = 0

while True:
    n:float = float(input("inserisci n: "))
    if n > 0:
        sum += n
    cont += 1
    if cont > 5:
        break

print(sum)
