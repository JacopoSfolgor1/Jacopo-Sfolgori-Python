'''Esercizio 8.

Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri 
compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''

def vowelsCounter(word:str = None):
    
    vowels:list[str] = ["a","e","i","o","u"]

    if not word:
        return 0
    
    if word[0].lower() in vowels:
        return 1 + vowelsCounter(word[1:])
    
    else:
        return 0 + vowelsCounter(word[1:])
    

print(vowelsCounter("ciao"))
print(vowelsCounter())