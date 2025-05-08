'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.'''

parola: str = input("scrivi la parola: ")
contatore: int = 0
for letter in parola: 
    if letter == " ": 
        contatore += 1 #aggiorno il contatore se sono presenti effetivamente degli spazi
print(f"{parola} ha: {contatore} spazi")