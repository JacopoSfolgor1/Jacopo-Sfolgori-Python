'''11. Sistema di prenotazione di posti

Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". Per ogni opzione:

se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''


liberi:int = 20

while True:
    opzione:str = input("inserisci opzione: ").lower()
    match opzione:
        
        case "prenota":
            if liberi > 0:
                liberi -= 1
            else:
                print("non ci sono posti liberi")

        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("tutti i posti sono già disponibili")
    
        case "visualizza":
            print(f"{liberi} liberi, {20 - liberi} occupati")
        
        case "fine":
            print("fine")
            break
    
    