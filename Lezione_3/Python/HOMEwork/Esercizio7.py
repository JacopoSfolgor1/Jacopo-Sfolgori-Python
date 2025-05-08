'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

a:list = [] 
b:list = []  
c:list = []  


i = int(input("Scegli quanti numeri aggiungere alle liste: "))  #input per sequenza numeri in lista a
i2:int = i  #copia per controllo sequenza numeri per lista b da indice a

while i > 0: 
    n1 = float(input("Inserisci il numero per lista a: ")) #creo numero per a
    if n1.is_integer():
        a.append(int(n1)) #aggiungo a lista a se intero convertendolo da float a int altrettanto
        i -= 1
    else: 
        print("Scegli un numero intero per la lista a")

while i2 > 0: 
    n2 = float(input("Inserisci il numero per lista b: ")) #creo numero per b
    if n2.is_integer():
        b.append(int(n2))  #aggiungo a lista b se intero
        i2 -= 1
    else: 
        print("Scegli un numero intero per la lista b")

n:int = len(a)  #creo la condizione per il controllo del ciclo annesso a c
for i in range(n):
    c.append(a[i] + (b[-(i+1)]-1))  #aggiungo in c i risultati in input di a e b in base al primo esempio a[1] + b[n-1]


print(f"Lista a: {a} \nLista b: {b} \nLista c: {c}")