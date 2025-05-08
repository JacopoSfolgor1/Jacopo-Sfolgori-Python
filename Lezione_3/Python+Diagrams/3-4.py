'''4. Assegnazione di un tutor
Progettare un algoritmo che assegni i 10 tutor disponibili agli studenti che necessitano di recupero in un istituto scolastico. 
Per ogni studente dato in input, il sistema deve controllare la disponibilità dei tutor e, nel caso di disponibilità, assegnarlo allo studente. 
Se il numero di tutor disponibili scende a zero, occorre aumentare il numero di studenti in lista d'attesa. Occorre confermare sia l’assegnazione 
del tutor con successo che l'inserimento nella lista d’attesa allo studente. 
L'algoritmo termina solo quando il numero di tutor è pari a 0 e la lista d'attesa conta 50 studenti. '''

n_tutor:int = 10

attesa:int = 0

while True:
    
    studente:str = input("inserisci nome studente: ")
    
    if n_tutor > 0:
        n_tutor -= 1
        print(f"tutor assegnato con successo a {studente}")
    
    elif attesa < 50:
            attesa += 1
            print(f"{studente} in attesa: {attesa}")
    else:
        if attesa > 50:
            print("numero tutor pari a 0 e lista di attesa con 50 studenti")
            break
    
    
