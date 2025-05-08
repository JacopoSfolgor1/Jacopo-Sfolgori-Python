'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

i:int = 0 #creo indice per controllare se input sono interi
while i < 2: 
    if i == 0: 
        n1: float = float(input("inserisci il primo numero: ")) #creo n1
        if n1.is_integer():
            i += 1
        else: 
            i = 0 
            print("scegli un numero intero")
    elif i == 1:
        n2: float = float(input("inserisci il secondo numero: ")) #creo n2
        if n2.is_integer():
            i += 1
        else:
            i = 1 #assicuro ciclo while i riparta con le condizioni giuste 
            print("scegli un secondo numero intero")

n1 = int(n1) #converto n1, n2 in interi da float perché altrimenti da errore
n2 = int(n2)
prodotto:int = 1 #creo prodotto
if n1 > n2: 
    for num in range(n2, n1 +1):
        prodotto *= num
else:
    for num in range(n1, n2 +1):
        prodotto *= num

print(f"{prodotto} il prodotto è questo")