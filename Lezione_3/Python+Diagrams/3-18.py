'''18. Classifica e somma condizionale

Scrivere un algoritmo che consenta all’utente di inserire una numero variabile di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
Mostrare in output entrambe le somme e indicare quale somma è maggiore.'''

while True:
    n = float(input("Inserisci n: "))
    if n % 1 == 0 and n > 0:  
        n = int(n)  
        break
    else:
        print("Serve un numero intero positivo")

i = 0
somma = 0
somma_pari = 0
somma_dispari = 0

while i < n:
    x = float(input("Inserisci numero: "))
    
    if x % 1 == 0:  
        x = int(x)  
        somma += x  
        i += 1  
        
        media = somma / i
        
        if x % 2 == 0 and x > media:
            somma_pari += x
        elif x % 2 != 0 and x < media:
            somma_dispari += x
    else:
        print("Numero deve essere intero")

print(f"Somma dispari: {somma_dispari}, Somma pari: {somma_pari}")

if somma_pari > somma_dispari:
    print(f"Somma pari {somma_pari} è maggiore")
elif somma_dispari > somma_pari:
    print(f"Somma dispari {somma_dispari} è maggiore")
else:
    print(f"Somme sono uguali: {somma_dispari}")