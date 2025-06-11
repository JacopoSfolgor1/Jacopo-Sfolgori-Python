'''Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''

def ricerca_binaria(lista: list[int], num: int):
    if not lista:
        return False

    centro: int = len(lista) // 2
    val: int = lista[centro]

    if val == num:
        return True
    elif val < num:
        return ricerca_binaria(lista[centro + 1:], num)
    else:
        return ricerca_binaria(lista[:centro], num)



num = [1, 3, 5, 7, 10, 14, 24, 66, 2378568]
print(ricerca_binaria(num, 66))   
print(ricerca_binaria(num, 34))   