'''
Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. 
Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Giulia Bianchi
Digitare ruolo dell'utente: utente
Digitare l'età dell'utente: 16
Output: Accesso limitato! Alcune funzionalità sono limitate!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Sara Neri
Digitare ruolo dell'utente: vip
Digitare l'età dell'utente: 22
Output: Attenzione! Ruolo non riconosciuto! Accesso Negato!

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Luca Verdi
Digitare ruolo dell'utente: moderatore
Digitare l'età dell'utente: 25
Output: Salve Luca Verdi! Può gestire i contenuti ma non modificare le impostazioni.
'''

categoria: dict = {"nome": "", "età" : 0, "ruolo" : ""}
nome: str = str(input("inserisci nome: ")).title()
categoria.update({"nome": nome})
età:int = int(input("inserisci età: "))
categoria.update({"età" : età})
ruolo: str = str(input("inserisci ruolo: ")).lower()
categoria.update({"ruolo" : ruolo})


match categoria: 
    
    case {"ruolo": "admin"}:
        print(f"Salve {nome} \nHai ruolo {ruolo}: Accesso completo a tutte le funzionalità.")
    
    case {"ruolo": "moderatore"} if età >= 18:
        print(f"Salve {nome} \nHai {età} anni: Accesso standard a tutti i servizi. \nHai ruolo {ruolo}: Può gestire i contenuti ma non modificare le impostazioni.")
    
    case {"ruolo": "moderatore"} if età < 18:
        print(f"Salve {nome} \nHai {età} anni: Accesso limitato! Alcune funzionalità sono bloccate. \nHai ruolo {ruolo}: Può gestire i contenuti ma non modificare le impostazioni.")
    
    case {"ruolo": "ospite"}:
        print(f"Salve {nome} \nHai ruolo {ruolo}: Accesso ristretto! Solo visualizzazione dei contenuti.")
    
    case _:
        print(f"Salve {nome} \n{ruolo}: Attenzione! Ruolo non riconosciuto! Accesso Negato!")


