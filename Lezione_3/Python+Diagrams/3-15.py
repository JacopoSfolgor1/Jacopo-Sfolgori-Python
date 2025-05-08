'''15. Calcolo di intervalli condizionati

Progettare un algoritmo che chieda all’utente di inserire un valore intero n.
L'algoritmo deve:

Verificare se n è compreso tra 1 e 100:
se sì, calcolare e mostrare la somma di tutti i numeri pari compresi tra 1 e n.
Verificare se n è 0 o negativo:
Se sì, mostrare un messaggio di errore e terminare.
Altrimenti, calcolare e mostrare la somma di tutti i numeri dispari compresi tra 1 e n.'''


while True:
    n = float(input("inserisci n: "))
    if n % 1 == 0:
        n = int(n)
        break
match n:  
    case n if n > 0 and n <= 100:
        sum = 0 
        for i in range(1,n+1):
            if i % 2 == 0:
                sum += 1
        print(f"{sum} è la somma pari")
    
    case n if n == 0 or n < 0:
        print("errore")
    
    case _:
        sum = 0
        for i in range(1,n+1):
            if i % 2 != 0:
                sum += 1
        print(f"{sum} è la somma dispari")