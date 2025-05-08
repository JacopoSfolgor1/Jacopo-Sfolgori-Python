import random

#creo tartaruga
def tartaruga(pos: int = 1, weather: str = "", stamina: int = 100):
    chance:int = random.randint(1, 10) 
    
    #aggiorno malus in base al meteo
    if weather == "pioggia":    
        malus: int = 1  
    else:
        malus = 0  

    match chance:
        
        #50% passo veloce
        case 1 | 2 | 3 | 4 | 5:         
            if stamina >= (5 + malus):  
                if pos < (68 - malus):  
                    pos += (3 - malus) 
                else:
                    pos = 70
                stamina -= (5 + malus)  
            else:
                stamina += 10 
        
        #30% passo lento
        case 6 | 7:                     
            if stamina >= (10 + malus): 
                if pos > (6 + malus): 
                    pos -= (6 + malus)  
                else:
                    pos = 1  
                stamina -= (10 + malus) 
            else:
                stamina += 10
        
        #20% riposo
        case _:                        
            if stamina >= (3 + malus):  
                if pos < (70 - malus):  
                    pos += (1 - malus)  
                else:
                    pos = 70  
                stamina -= (3 + malus)  
            else:
                stamina += 10 
    
    return pos, stamina

#creo lepre
def lepre(pos: int = 1, weather: str = "", stamina: int = 100):
    chance: int = random.randint(1, 10)
    
    #aggiorno malus in base al meteo
    if weather == "pioggia":   
        malus: int = 1 
    else:
        malus = 0
    
    match chance:
        
        #20% riposo
        case 1 | 2:            
            if stamina <= 90:
                stamina += 10        
        
        #20% grande balzo
        case 3 | 4:             
            if stamina >= (15 + malus):
                if pos < (62 + malus):
                    pos += (9 - malus) 
                else:
                    pos = 70 
                stamina -= (15 + malus)  
            else:
                stamina += 10
        
        #10% grande scivolata
        case 5:                 
            if stamina >= (20 + malus):
                if pos > (12 + malus):
                    pos -= (12 + malus)  
                else:
                    pos = 1
                stamina -= (20 + malus)  
            else:
                stamina += 10
        
        #30% piccolo balzo
        case 6 | 7 | 8:         
            if stamina >= (5 + malus):
                if pos < (70 + malus):
                    pos += (1 - malus)  
                else:
                    pos = 70  
                stamina -= (5 + malus)
            else:
                stamina += 10
        
        #20% piccola scivolata
        case _:                  
            if stamina >= (8 + malus):
                if pos <= 3:
                    pos = 1
                else:
                    pos -= (2 + malus)
                stamina -= (8 + malus)
            else:
                stamina += 10
    
    return pos, stamina

#creo output gara
def gara(posH: int, posT: int, ostacoli: dict, bonus: dict):
    
    #creo lista '_' * 70
    quadrati:list = ["_" for i in range(70+1)]  
    
    #controllo se stessa posizione e non di partenza
    if posH == posT and posH > 1 and posT > 1: 
        
        word: str = "OUCH!!!"
        for i in range(len(word)):              
            pos = posH + i
            quadrati[pos] = word[i]

    else:
        quadrati[posH] = "H" 
        quadrati[posT] = "T" 
    
    #check for obstacles and bonuses for tortoise
    if posT in ostacoli:               
            
        print(f"!!!!! NOOOO !!!!! TARTARUGA ENCOUNTERED AN OBSTACLE AT POSITION {posT} !!!!!")
        print("_ " * 71)
        print("_ " * 71)
        
        posT += ostacoli[posT]
        if posT < 1:
            posT = 1
            
    #check for bonuses for tortoise
    elif posT in bonus:                 
        
        print(f"!!!!! OH YES !!!!!! TARTARUGA ENCOUNTERED A BONUS AT POSITION {posT} GO TARTA GO !!!!!")
        print("_ " * 71)
        print("_ " * 71)

        
        posT += bonus[posT]
        if posT > 70:
            posT = 70
            
    #check for obstacles and bonuses for hare
    if posH in ostacoli:               
        print(f"!!!!! NOOOO !!!!! LEPRE ENCOUNTERED AN OBSTACLE AT POSITION {posH} !!!!!")
        print("_ " * 71)
        print("_ " * 71)
        posH += ostacoli[posH]
        if posH < 1:
            posH = 1
        
    #check for bonuses for hare
    elif posH in bonus:                
        print(f"!!!!! OH YES !!!!!! LEPRE ENCOUNTERED A BONUS AT POSITION {posH} GO BUNNY GO !!!!!")
        print("_ " * 71)
        print("_ " * 71)
        posH += bonus[posH]
        if posH > 70:       
            posH = 70
           
    #stampo il tutto aggiornato ogni volta si chiama la funzione
    print(" ".join(quadrati))
    return posH, posT

#controllo se partita da rifare in caso di pareggio
while True:     
    
    #creo bonus e ostacoli 
    ostacoli: dict = {15: -3, 30: -5, 45: -7}
    bonus: dict = {10: 5, 25: 3, 50: 10}
   
    #inizializzo variabili per far partire il tutto 
    posH: int = 1    
    posT: int = 1
    orologio: int = 0
    mpH: int = 100
    mpT: int = 100
    
    #rifinizione output pulito e ordinato per ogni statistica da controllare 
    print("_ " * 71)                               
    print("!!!!! STARTING POSITIONS !!!!!")
    gara(posH, posT, ostacoli, bonus)
    
    print(f"!!!!! STARTING STAMINA IS 100 FOR EACH CONTESTANT !!!!!")
    print("_ " * 71)
    
    print(f"!!!!! STARTING WEATHER !!!!!: !!!!! soleggiato !!!!!")
    print("_ " * 71)
    
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    #controllo se vittoria
    while posH < 70 and posT < 70:          
        
        #controllo se pari o dispari e cambiare meteo di conseguenza
        if orologio // 10 % 2 == 0:
            weather = "soleggiato"
        else:
            weather = "pioggia"
        
        #stampo in output il cambio meteo
        if orologio % 10 == 0 and orologio >= 10:
            print(f"Weather changed to: {weather}")
            print(f"Tick: {orologio}")

        else:
            #stampo solo altrimenti a quale tick siamo
            print(f"Tick: {orologio}")

        #aggiorno tick
        orologio += 1
        
        
        #aggiorno le variabili per tartaruga salvandone i valori 
        posT, mpT= tartaruga(posT, weather, mpT)
        
        print(f"Tartaruga: {posT}° posizione, stamina: {mpT} mp")
    
        #aggiorno le variabili per lepre salvandone i valori 
        posH, mpH = lepre(posH, weather, mpH)    
        
        print(f"Lepre: {posH}° posizione, stamina: {mpH} mp")
        print("_ " * 71)

        posH, posT = gara(posH, posT, ostacoli, bonus)
        print("_ " * 71)

    #controllo condizione di vittoria in caso di pareggio non fa break e ricomincia
    if posH == 70 and posT == 70:
        
        print("IT'S A TIE! NEXT MATCH IS UP NOW!!!")    
    
    elif posH == 70:    
        print("HARE WINS")
        print("YUCH!!!")
        break
    
    elif posT == 70:    
        print(f"TORTOISE WINS!")
        print("VAY!!!")
        break

