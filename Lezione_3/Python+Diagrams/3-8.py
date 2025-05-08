'''8. Determinare la somma dei numero dentro un intervallo

Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. 
Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. Se i valori sono validi, 
calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.'''


a:int = int(input("inserisci a: "))
b:int = int(input("inserisci b: "))

if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            sum_ab:int = 0
            i:int = a
            for i in range(b+1):
                sum_ab += i
            print(sum_ab)
else:
    print("valori non richiesti")