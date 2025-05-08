'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

parola: str = input("inserisci parola: ")
reverse: str = ""  
for letter in parola:
    reverse = letter + reverse  #dopo vari tentativi soprattutto illogici, ho pensato di aggiungere la lettera + reverse per indicare un ordine sommatorio al ciclo, è però un concetto che vorrei afferrare maggiormente

print(parola, reverse)
