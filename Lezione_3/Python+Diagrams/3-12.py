'''12. Scelta condizionale basata su input multipli

Progettare un algoritmo che richieda all’utente di inserire un numero variabile n di valori x e y. L'algoritmo deve:

    calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
    calcolare la somma di x e y solo se uno dei due valori è negativo;
    mostrare il risultato dell’operazione effettuata o un messaggio di errore altrimenti.
'''

n:int = int(input("inserisci n sequenza: "))

i:int = 0

for i in range(n):
    x:int = int(input("inserisci x: "))
    y:int = int(input("inserisci y: "))
    if x > 0 and y > 0:
        result:int = x * y
        print(result)
    else:
        if x < 0 and y < 0:
            print("errore")
        else:
            result:int = x - y 
            print(result)