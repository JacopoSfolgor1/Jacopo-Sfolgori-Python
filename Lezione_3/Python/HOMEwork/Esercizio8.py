'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) 
e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******'''
i = 0
sequenza:list = []
output: str = "*"

while i < 5:
    n = float(input("inserisci un numero: "))
    if n.is_integer() and n in range(1,30+1): #controllo se numero intero e in range fra 1 e 30
        i += 1
        sequenza.append(int(n)) #aggiungo numeri a lista e li converto da float a interi
    else:
        print("inserisci un numero intero e fra 1 e 30!")

for n in sequenza:
    print(output * n)

