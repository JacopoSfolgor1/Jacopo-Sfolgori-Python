'''1. Sistema di gestione per un parcheggio
Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio con un numero massimo di posti dato in input. 
L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:

    se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
    se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.

Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

max_parcheggi:int = int(input("inserisci numero parcheggio max: "))

liberi:int = max_parcheggi

word: str = input("inserisci opzione: ").lower()
while word != "esci":
    match word:
        case "ingresso":
            if liberi > 0:
                liberi -= 1 
            else:
                print("non ci sono posti disponibili")

        case "uscita":
            if liberi < max_parcheggi:
               liberi += 1
            else:
                print("Tutti i posti sono già disponibili")

        case "stato":
            print(f"{liberi} posti liberi, posti totali {max_parcheggi}")
    word: str = input("inserisci opzione: ").lower()