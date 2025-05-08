'''11. Classifica basata su più condizioni

Progettare un algoritmo che richieda all’utente di inserire un valore intero.
Il programma deve verificare:

    se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
    se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.
'''



i = 0

while i == 0:
    n:int = float(input("inserisci n: "))
    if n % 1 == 0:
        i += 1
    else:
        print("numero deve essere intero")


if n % 2 == 0 and n > 10:
    print("numero valido")
else:
    print("numero non valido")