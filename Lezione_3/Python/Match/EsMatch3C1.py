'''
Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto: 5
Output: Insufficiente
- - - - - - - - - - -
Inserisci il voto: 11
Output: Voto non valido
'''

i = 0
while i < 1:
    voto:float = float(input("Dai il voto da 1 a 10: "))
    if voto.is_integer() and voto in range(1,10+1):
        int(voto)
        match voto:
            case 1 | 2 | 3:
                print(f"{voto} è gravemente insufficiente")
            case 4 | 5:
                print(f"{voto} insufficiente")
            case 6 | 7:
                print(f"{voto} sufficiente")
            case 8 | 9:
                print(f"{voto} molto buono")
            case 10:
                print(f"{voto} eccellente")
            case _:
                print(f"Voto non valido")
        i +=1
    else:
        print("Voto non valido")
        



voto:int = int(input("Dai il voto da 1 a 10: "))
match voto:
        case 1 | 2 | 3:
            print(f"{voto} è gravemente insufficiente")
            
        case 4 | 5:
            print(f"{voto} insufficiente")
               
        case 6 | 7:
            print(f"{voto} sufficiente")
                
        case 8 | 9:
            print(f"{voto} molto buono")
              
        case 10:
            print(f"{voto} eccellente")
               
        case _:
            print(f"Voto non valido")
                
                

