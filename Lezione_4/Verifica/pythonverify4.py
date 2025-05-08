'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    dict3:dict = {}
    for key,value in dict1.items():
        if key in dict2:
            dict3.update({key:value+dict2[key]})
        else:
            dict3.update({key:value})
    
    for key,value in dict2.items():
        if key in dict1:
            dict3.update({key:value+dict2[key]})
        else:
            dict3.update({key:value})
                
    return dict3

print(merge_dictionaries({'x': 5}, {'x': -5}))
 	

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))