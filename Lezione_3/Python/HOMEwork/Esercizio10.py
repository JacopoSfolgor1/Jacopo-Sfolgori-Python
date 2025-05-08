'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''


list_n: list = []
pari:int = 0
dispari:int = 0
i:int = 0
freq: dict = {} #creo una lista per salvare i numeri e il loro valore di ripetizione
while True:  
        n: float = float(input("inserisci il numero: "))
        if n == 0:
            break #interrompo input di dare n se equivale a 0
        if n.is_integer():
                list_n.append(int(n)) #aggiungo i numeri alla lista convertiti in intero
                if n % 2 == 0:
                    pari += n
                else:
                    dispari += n
                    i += 1                  
                if n in freq: #aggiungo a frequenza (freq) il numero
                    freq[n] += 1
                else:
                    freq[n] = 1
        else: 
            print("scegli un numero intero")

if i > 0:
    media_dispari = dispari / i #controllo se ci sono stati dispari in sequenza o meno
else:    
    media_dispari = 0

print(f"{list_n} lista n, {pari} somma pari, {media_dispari} media dispari") 

max_freq:int = 0 #creo variabile per frequenza massima
for key, value in freq.items(): #controllo chiave, valore di freq e aggiorno il valore appena creato max_freq
    if value > max_freq:
          max_freq = value

for key, value in freq.items(): #dopo il ciclo che aggiorna il massimo, controllo quale numero sia effettivamente
     if max_freq == value:
          print(f"Numero più frequente: {key}, {value} volte")




