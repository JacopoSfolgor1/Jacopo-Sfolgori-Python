'''9 . Conteggio dei numeri divisibili

Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n. Se n è negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

    l’utente può inserire 10 numeri interi;
    contare quanti di questi numeri sono divisibili per n.

Mostrare in output il risultato del conteggio.'''

n:int = int(input("inserisci n: "))

if n > 0:
    if n % 1 == 0:
        cont:int = 0
        i:int = 0
        for i in range(10):
            x:int = int(input("inserisci numero: "))
            if x % 1 == 0:
                cont += 1
        print(cont)
else:
    print("numero deve essere intero e positivo")