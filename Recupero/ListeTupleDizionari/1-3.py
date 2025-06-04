''''Liste, Tuple e Dizionari
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''


def convert(ky, val):
    check: dict = {}
    if ky in check:
        check[ky] += check[val]
    else:
        check.append(ky,val)
        

def separate(lnum: list):
    pos: list = []
    neg: list = []
    dizio: dict = {pos, neg}
    
    for n in range(len(lnum)):
        if n % 2 == 0:
            pos.append(n)
        else:
            neg.append(n)

    return dizio    

def prezzi(dicpro: dict):
    new: dict = {}
    for key,value in dicpro.items():
        if value < 50:
            newval = round((value * 10 ) / 100, 2)
            new.append(key,newval)

    return new