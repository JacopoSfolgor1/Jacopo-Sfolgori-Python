'''14. Simulazione di un gioco di dadi

Progettare un algoritmo che simuli un gioco basato sul lancio di due dadi virtuali a sei facce, D1 e D2. 
L'algoritmo deve eseguire le seguenti operazioni:

    Simulare il lancio dei due dadi.
    Calcolare la somma dei valori ottenuti dai due dadi.
    Applicare le seguenti regole di gioco per determinare il punteggio:
        Se entrambi i dadi mostrano numeri pari e la somma è maggiore di 8, il giocatore vince e il punteggio è impostato direttamente a 100.
        Se uno dei dadi mostra 6 oppure la somma è uguale a 7, il punteggio del giocatore viene incrementato di 10.
        In tutti gli altri casi, il giocatore perde e il punteggio è impostato a 0.
    Mostrare il risultato del gioco e il punteggio ottenuto.

Il gioco continua finché il punteggio totale del giocatore non raggiunge 100 (vittoria) oppure scende a zero (sconfitta).'''

#metodo while

punteggio: int = 0

while punteggio < 100:
    
    d1:int = int(input("inserisci d1: "))
    d2:int = int(input("inserisci d2: "))
    
    if d1 in range(1,6+1) and d2 in range(1,6+1):
        sum_d:int = d1+d2
    else:
        d1:int = int(input("inserisci d1: "))
        d2:int = int(input("inserisci d2: "))
    
    match d1,d2,sum_d:

        case d1,d2,sum_d if d1 % 2 == 0 and d2 %2 == 0 and sum_d > 8:
            punteggio += 100
    
        case d1,d2,sum_d if d1 == 6 or d2 == 6 or sum_d == 7:
            punteggio += 10
        
        case _:
            punteggio = 0 
            print("sconfitta")
            break
else:
    print("vittoria",punteggio)            
    
    