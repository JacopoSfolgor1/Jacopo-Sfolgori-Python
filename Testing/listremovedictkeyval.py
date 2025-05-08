def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # cancella pass e scrivi il tuo codice
    risultato:list[int] = []
    cont: dict[int:int] = da_rimuovere.copy()

    for i in lista:
        if i in cont and cont[i] > 0:
            cont[i] -= 1
        else:
            risultato.append(i)
    
    return risultato



print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))

#OUTPUT[1, 3, 4]