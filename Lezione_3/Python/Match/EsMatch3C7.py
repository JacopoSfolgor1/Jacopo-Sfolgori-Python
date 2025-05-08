'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%

'''

moneta:int = 0
testa:float = 0
croce:float = 0

risultato: str = str(input("Inserisci risultato lancio moneta 't' (testa) o 'c' (croce): ")).lower()
                  
while moneta < 8:
    match risultato:
        
        case "t":
            print("è uscito testa")
            testa += 1
            moneta += 1
        
        case "c":
            print("è uscito croce")
            croce += 1
            moneta += 1
        
        case _:
            print(f"Non so che risultato sia questo {risultato}")
    
    risultato: str = str(input("Inserisci risultato lancio moneta 't' (testa) o 'c' (croce):")).lower()

endcroce:float = (croce / 8) * 100
endtesta:float = (testa / 8) * 100

print(f"Croce è uscito: {croce} volte \n{endcroce:.2f} è la % \n Testa è uscito: {testa} volte \n{endtesta:.2f} è la %")

    
