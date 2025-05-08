'''
2. Automazione di un semaforo intelligente
Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. 
Questo sistema deve adattare i tempi di durata (espressi in percentuale) del verde in base al numero di veicoli presenti sulle principali direzioni 
di traffico: Nord-Sud ed Est-Ovest. Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.

Requisiti:

    Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli), quella direzione riceve un tempo minimo garantito per il verde 
    (es. 60%) e il restante tempo è assegnato all'altra direzione.
    Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
    Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente al numero totale di veicoli nelle due direzioni.

Stampare la percentuale del tempo assegnato al verde per ciascuna direzione.'''

nord_sud: int = int(input("inserisci nord sud: "))

est_ovest: int = int(input("inserisci est ovest: "))

soglia: int = 70

check = [nord_sud,est_ovest,soglia]

match check:
    
    case check if nord_sud > soglia and est_ovest > soglia:
        time_ns:int = 50
        time_eo:int = 50
    
    case check if nord_sud > soglia:
        time_ns:int = 60
        time_eo:int = 40
    
    case check if est_ovest > soglia:
        time_eo:int = 60
        time_ns:int = 40

    case _:
        print("uyguyyuuy")
        time_eo:int = (est_ovest/(nord_sud + est_ovest)) * 100 
        time_ns:int = (nord_sud/(nord_sud + est_ovest)) * 100

print(f"{time_ns} è il tempo assegnato ai semafori nord e sud \n{time_eo} è il tempo assegnato ai semafori est ed ovest ")
    