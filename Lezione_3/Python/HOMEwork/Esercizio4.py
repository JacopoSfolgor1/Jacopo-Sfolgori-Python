'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

numbers = float(input("scegli il numero: ")) 
n_list: list = [] 
somma:float = 0 
i:float = 0 
n_min = float("inf") #essendoci stato il concetto per min e max INF e -INF spiegato, ho imparato come ricrearlo in python
n_max = float("-inf")

while numbers > 0: 
    n_list.append(numbers) 
    if numbers > n_max: 
        n_max = numbers
    if numbers < n_min: 
        n_min = numbers
    if numbers.is_integer(): #controllo per i numeri interi e calcolo della media conseguente, ho sofferto per capire come utilizzare .is_integer()
        somma += numbers
        i += 1
    numbers = float(input("scegli il numero: ")) #per continuare ad aggiunger numeri finché condizione while

if i > 0: #controllo nell'effettivo ci siano numeri interi in lista
    media:float = somma / i #se ci sono interi, calcolo la media e creo la variabile per salvarla
else: 
    media = 0 

print(f"{n_list} lista totale dei numeri \n{media} media dei numeri interi \n{n_max} numero massimo inserito \n{n_min} numero minimo inserito")



