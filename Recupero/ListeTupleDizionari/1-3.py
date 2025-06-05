''''Liste, Tuple e Dizionari
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''


def convert(lst: list[tuple]):
    check = {}
    for key, val in lst:
        if key in check:
            check[key] += val
        else:
            check[key] = val
    return check

        

def separate(lnum: list):
    pos = []
    neg = []
    for n in lnum:
        if n >= 0:
            pos.append(n)
        else:
            neg.append(n)
    return {"positivi": pos, "negativi": neg}

def prezzi(dicpro: dict):
    new = {}
    for key, value in dicpro.items():
        if value < 50:
            newval = round(value * 1.10, 2)
            new[key] = newval
    return new