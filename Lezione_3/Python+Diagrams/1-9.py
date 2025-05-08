'''9. Classifica delle vendite

Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori, trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.'''


nome:str = input("inserisci nome: ")
vendite:int = int(input("inserisci vendite: "))

max_nome: str = nome
max: int = vendite

min_nome: str = nome
min: int = vendite 

cont: int = 0

for cont in range(1,19+1):
    new_nome:str = input("inserisci nome: ")
    new_vendite:int = int(input("inserisci vendite: "))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    else:
        if new_vendite < min:
            min_nome = new_nome
            min = new_vendite
print(f"{max} è il n massimo di nome {max_nome}, {min} è il minimo di nome: {min_nome}")



