# Lezione02 Esercizio 1-4
''' 1-4. Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, 
lo si visualizzi, una cifra per riga:

2
0
2
4 '''

numero = 2024 
print(numero//1000) # 1st digit
print((numero//100)%10) #2nd digit
print((numero//10)%10) #3rd digit
print(numero%10) #4th digit