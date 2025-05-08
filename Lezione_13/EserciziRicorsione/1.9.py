'''Esercizio 9.

Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.'''

def vowelRemover(text: str) -> str:
    
    vowels:list[str] = ["a","e","i","o","u"]
    
    if not text:
        return ""

    if text[0].lower() in vowels:
        return vowelRemover(text[1:])
    else:
        return text[0] + vowelRemover(text[1:])
    
print(vowelRemover("ciao come stai"))

print(vowelRemover(""))