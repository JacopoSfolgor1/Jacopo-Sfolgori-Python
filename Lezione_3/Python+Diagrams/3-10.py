'''10. Validazione dell'età per l'attività

Progettare un algoritmo che richieda all’utente di inserire la sua età.
L'algoritmo deve:

    controllare se l’età è compresa tra 18 e 65 anni. Se sì, mostrare un messaggio che indica che l’utente può partecipare all’attività;
    se l’età non rientra nell’intervallo, verificare se è inferiore a 18 oppure maggiore di 65. Se sì, mostrare un messaggio 
    che indica che l’utente non può partecipare perché ha superato l'età massima consentita o non ha raggiunto l'età minima consentita.
'''

età: int = int(input("inserisci età: "))

if età in range(18,65+1):
    print("puoi partecipare")
else:
    if età < 18:
        print("non hai raggiunto età minima")
    
    else:
        print("hai superato l'età per partecipare")
    
