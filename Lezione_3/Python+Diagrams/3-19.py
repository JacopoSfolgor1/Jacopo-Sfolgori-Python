'''19. Calcolo di sequenze condizionali

Scrivere un algoritmo che calcoli il valore di una sequenza numerica basata su un valore n inserito dall’utente. La sequenza segue queste regole:

se n è pari, calcolare la somma dei numeri da 1 a n che sono divisibili per 4;
se n è dispari, calcolare il prodotto dei numeri dispari da 1 a n;
se n è negativo, mostrare un messaggio di errore e terminare.
Infine, mostrare il risultato calcolato.'''

while True:
    n = float(input("Inserisci n: "))
    
    if n < 0:
        print("Errore: n è negativo")
        break  
    
    if n % 1 == 0 and n > 0:
        n = int(n)  
        break
    else:
        print("Serve un numero intero positivo")

if n > 0:

    if n % 2 == 0:
        cont = 4
        result = 0
        while cont <= n:
            result += cont
            cont += 4
        print(f"{result} pari")
    
    else:
        cont = 1 
        result = 1 
        while cont <= n:
            result *= cont
            cont += 2
        print(f"{result} dispari")
    

