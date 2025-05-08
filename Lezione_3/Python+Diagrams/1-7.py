'''7. Conta i numeri pari e dispari

Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.'''

pari:int = 0
dispari:int = 0
cont:int = 0

for cont in range(1,10+1):
    n:int = int(input("inserisci numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1

print(pari, dispari)
