'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini 
sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.

'''
list_pi: list = [3.14, 3.141, 3.1415, 3.14159] #creo lista per controllo dei vari pi
n1:int = 4
n2:int = 1
pi_app: float = 0
i:int = 0

for pi in list_pi: #itero su sequenze pi in lista
    while abs(pi_app - pi) > 0.00005: #per comprendere come sfruttare al meglio abs ci ho messo molto, soprattutto per capire come aggiungere una condizione funzionante nel ciclo
        if i % 2 == 0:  #se l'iterazione è pari aggiunge a pi app la sequenza con addizione, altrimenti sottrae la sequenza
            pi_app += n1 / n2
        else:
            pi_app -= n1 / n2
        n2 += 2
        i += 1
    print(f"Per approssimare {pi}, hai bisogno di: {i} sequenze")