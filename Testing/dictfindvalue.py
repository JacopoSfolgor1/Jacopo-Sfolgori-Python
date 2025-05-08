def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    # cancella pass e scrivi il tuo codice
    for key,value in dizionario.items():
        if value == valore:
            return key
    return None

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))