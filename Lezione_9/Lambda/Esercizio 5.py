'''Esercizio 5 – Funzione lambda con if

Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".'''

numero: int = lambda x : "pari" if x % 2 == 0 else "dispari"

print(numero(24))

print(numero(23))