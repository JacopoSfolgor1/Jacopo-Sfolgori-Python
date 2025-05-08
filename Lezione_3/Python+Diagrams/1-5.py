'''5. Verifica se un numero è primo

Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo.'''

n:int = int(input("inserisci n se n primo o no: "))
div:int = 0
primo: bool = True

if n < 2:
    primo = False
    print("numero non primo")
else:
    div = 2
    while div < 2:
        if n % div != 0:
            div += 1
        else:
            primo = False
            break

if primo == True:
    print("Primo")
else: 
    print("non primo")

