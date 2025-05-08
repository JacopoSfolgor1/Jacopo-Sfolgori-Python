'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di 
inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica 
'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, 
deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, 
il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

mammiferi:list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"] 
pesci:list = ["squalo", "trota", "salmone", "carpa"]

animal:str = str(input("Inserisci il nome animale: ")).lower()
habitat: str = str(input("Inserisci l'habitat dell'animale: ")).lower()

animal_type: str = ""

match animal:
    #mammiferi
    case animal if animal in mammiferi:
        print(f"{animal} appartiene alla categoria mammiferi!")
        animal_type = "mammifero"
    #rettili
    case animal if animal in rettili:
        print(f"{animal} appartiene alla categoria rettili!")
        animal_type = "rettile"
    #uccelli
    case animal if animal in uccelli:
        print(f"{animal} appartiene alla categoria uccelli!")
        animal_type = "uccello"
    #pesci
    case animal if animal in pesci:
        print(f"{animal} appartiene alla categoria pesci!")
        animal_type = "pesce"
    #unknown
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animal}")
        animal_type = "unknown"

info: dict = {"nome": animal, "tipo": animal_type, "habitat": habitat}

match info:
    #mammiferi
    case {"nome": value, "tipo": "mammifero", "habitat": value2} if value not in ["delfino", "balena"] and value2 == "terra":
        print(f"{animal} è un {animal_type} e va su {habitat}") 
    case {"nome": value, "tipo": "mammifero", "habitat": value2} if value not in ["delfino", "balena"] and value2 != "terra":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    case {"nome": value, "tipo": "mammifero", "habitat": value2} if value in ["delfino", "balena"] and value2 == "acqua":
        print(f"{animal} è un {animal_type} e va su {habitat}")
    case {"nome": value, "tipo": "mammifero", "habitat": value2} if value in ["delfino", "balena"] and value2 != "acqua":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    #rettili
    case {"tipo": "rettile", "habitat": value} if value != "aria":
        print(f"{animal} è un {animal_type} e va su {habitat}")
    case {"tipo": "rettile", "habitat": value} if value == "aria":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    #uccelli
    case {"nome": value, "tipo": "uccello", "habitat": value2} if value in ["aquila", "pappagallo", "gufo", "falco"] and value2 == "aria":
        print(f"{animal} è un {animal_type} e va su {habitat}")
    case {"nome": value, "tipo": "uccello", "habitat": value2} if value in ["aquila", "pappagallo", "gufo", "falco"] and value2 != "aria":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    case {"nome": value, "tipo": "uccello", "habitat": value2} if value not in ["aquila", "pappagallo", "gufo", "falco"] and value2 == "aria":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    case {"nome": value, "tipo": "uccello", "habitat": value2} if value not in ["aquila", "pappagallo", "gufo", "falco"] and value2 != "aria":
        print(f"{animal} è un {animal_type} e va su {habitat}")
    #pesci
    case {"tipo": "pesce", "habitat": value} if value == "acqua":
        print(f"{animal} è un {animal_type} e va su {habitat}")
    case {"tipo": "pesce", "habitat": value} if value != "acqua":
        print(f"{animal} è un {animal_type} e NON va su {habitat}")
    #unknown
    case _:
        print(f"{animal} tipo: {animal_type} non so classificarlo né dare info su habitat: {habitat}")