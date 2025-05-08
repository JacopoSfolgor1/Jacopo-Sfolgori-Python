'''4. Controllo della parità di un numero

Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari.'''

n:int = int(input("inserisci n: "))

if n % 2 == 0:
    print("pari")
else: 
    print("dispari")