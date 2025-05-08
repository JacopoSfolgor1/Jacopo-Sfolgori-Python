'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

parola:str = input("scrivi la parola: ").lower() #inserire la parola con .lower in maniera tale che se viene inserita "FINE" arrivo facilmente alla conclusione
while parola != "fine":
    if parola[0] == parola[-1]:
        print(f"{parola} ha lettera iniziale e finale uguale")
    else:
        print(f"{parola} ha lettera iniziale e finale disuguale") 
    parola = input("scrivi un'altra parola: ").lower() #per continuare ad aggiungere parole fino a quando non si arriva alla parola fine
print("hai finito le parole") 