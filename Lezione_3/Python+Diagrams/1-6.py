'''6. Calcolo del fattoriale di un numero

Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.'''

n:int = int(input("inserisci numero: "))

if n % 1 == 0 and n > 0: 
    fattoriale:int = 1 
else:
    print("il numero inserito deve essere intero e positivo")



for i in range(1,n+1): 
    fattoriale *= i 
    
print(fattoriale)