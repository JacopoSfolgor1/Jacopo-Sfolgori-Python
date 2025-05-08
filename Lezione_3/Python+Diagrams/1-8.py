'''8. Trovare i numeri maggiori di un valore soglia

Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.'''


soglia:int = int(input("scegli soglia: "))

cont:int = 0

for cont in range(1,7+1):
    n:int = int(input("numero: "))
    if n > soglia:
        print(f"{n} è maggiore di {soglia}")


