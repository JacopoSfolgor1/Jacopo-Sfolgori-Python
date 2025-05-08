# Lezione02 Esercizio 1-1
''' 1-1. Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:
     Memorizzare un numero in virgola mobile nella variabile x.
     Calcolare 1.0/x memorizzare il risultato nella variabile y.
     Visualizzare il valore di x, y e il prodotto tra x e y.
     Sottrarre x dal prodotto tra x e y e mostrarne il risultato. '''
     
x:float = 4.25
y = (1.0/x)

print(f"il valore di x e' : {x} \n il valore di y e': {y:.2f}")
print(f"\n Il prodotto fra x e y vale: {x * y}")

print(f"x*y-x: {x*y-x}") # modo 1

# modo 2
z = x * y
print(z - x)