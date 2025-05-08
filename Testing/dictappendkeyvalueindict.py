def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    # cancella pass e scrivi il tuo codice
    filtrato: dict[str, float] = {}
    
    for nome, prezzo in prodotti.items():
        if prezzo > 20:
            scontato = prezzo * 0.90  
            filtrato[nome] = scontato
    
    return filtrato


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

	

#{'Zaino': 45.0, 'Quaderno': 19.8}

print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 

	

#{}