'''5. Calcolo della somma dei quadrati fino a un numero intero positivo n

Progettare un algoritmo che, dato un numero intero positivo n definito dall'utente, calcoli la somma:

12 + 22 + 32 + 42 + 52 + ... + n2,

mostrando in output il risultato. Se n è negativo, l'algoritmo mostra un messaggio di errore e termina. '''


n:int = int(input("inserisci n: "))

    
if n % 1 == 0 and n > 0:
    sum_n = 0
    i = 1
    for i in range(n+1):
        sum_n += i*i
    print(sum_n)
else:
    print("Errore numero deve essere positivo")       
    
    
