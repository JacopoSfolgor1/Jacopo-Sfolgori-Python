'''13. Esercizio di controllo numerico con condizioni arbitrarie

Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

    la somma di x+y+z deve essere pari;
    x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
    se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare: “Regole non rispettate”.
'''


i:int = 0

while i < 3:
    
    if i == 0:    
        x:int = int(input("inserisci x: "))
        if x % 1 == 0 and x > 0:
            i = 1
        else:
            print("x deve essere intero e positivo")
    
    if i == 1:
        y:int = int(input("inserisci y: "))
        if y % 1 == 0 and y > 0:
            i = 2
        else:
            print("y deve essere intero e positivo")
    if i == 2:
        z:int = int(input("inserisci z: "))
        if z % 1 == 0 and z > 0:
            i = 3
        else:
            print("z deve essere intero e positivo")

if x+y+z % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z & 7 ==0:
    print("regole rispettate")
else:
    print("regole non rispettate")

