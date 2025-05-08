'''
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per 
determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido
'''

laurea_voto:int = int(input("inserisci il voto di laurea: "))

match laurea_voto:
    case laurea_voto if laurea_voto in range(106,110+1):
        print(f"{laurea_voto} è 4.0 in GPA")
    case laurea_voto if laurea_voto in range(101,105+1):
        print(f"{laurea_voto} è 3.7 in GPA ")
    case laurea_voto if laurea_voto in range(96,100+1):
        print(f"{laurea_voto} è 3.3 in GPA ")
    case laurea_voto if laurea_voto in range(91,95+1):
        print(f"{laurea_voto} è 3.0 in GPA")
    case laurea_voto if laurea_voto in range(86,90+1):
        print(f"{laurea_voto} è 2.7 in GPA ")
    case laurea_voto if laurea_voto in range(81,85+1):
        print(f"{laurea_voto} è 2.3 in GPA")
    case laurea_voto if laurea_voto in range(76,80+1):
        print(f"{laurea_voto} è 2.0 in GPA")
    case laurea_voto if laurea_voto in range(70,75+1):
        print(f"{laurea_voto} è 1.7 in GPA")
    case laurea_voto if laurea_voto in range(66,69+1):
        print(f"{laurea_voto} è 1.0 in GPA")
    case _:
        print("Voto non valido")

