def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice
    votidict: dict[str:list[int]] = {}
    for i in voti:
        nome = i["nome"]
        voto = i["voto"]
        
        if nome not in votidict:
            votidict[nome] = []
        votidict[nome].append(voto)
    
    return votidict


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

	

#{'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([])) 

#{}