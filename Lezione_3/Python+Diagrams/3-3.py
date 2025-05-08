'''3. Sistema di registrazione degli studenti a corsi
Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi disponibili in una università. Per ogni corso ci sono un massimo di 
100 posti liberi. Richiesto il nome del corso, mostra un menu con le seguenti opzioni "iscrivi", "annulla", "visualizza", "elimina", ed "Esci".

    se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "annulla", decrementa il numero di posti occupati;
    se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
    se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
    se l'utente inserisce "esci", termina l'algoritmo.
'''


nome_corso:str = input("inserisci nome corso: ").lower()

max_posti:int = 100

opzione:str = input("inserisci opzione: ").lower()

while opzione != "esci":
    match opzione:
        
        case "iscrivi":
            if max_posti > 0:
                max_posti -= 1
            else:
                print("non ci sono posti")
        
        case "annulla":
            if max_posti < 100:
                max_posti += 1
            else:
                print("già disponibili tutti posti")

        case "visualizza":
            print(f"{100 - max_posti} posti disponibili")
        
        case "elimina":
            new_nome_corso:str = input("inserisci nuovo nome corso: ")

        case _:
            print("opzione non valida")

    opzione:str = input("inserisci opzione: ").lower()