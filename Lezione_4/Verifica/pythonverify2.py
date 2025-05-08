'''Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.'''
def count_isolated(elements:list[int]) -> int:
    # cancella ... e definisci parametri e tipo di dato, successivamente cancella pass e scrivi il tuo codice
    c:int = 0
    for element in range(len(elements)):
        if element == 0 and elements[element+1] != elements[element]:
            c += 1
        elif element < len(elements)-1:
            if elements[element] != elements[element+1] and elements[element] != elements[element-1]:
                c += 1
        else:
            if elements[element] != elements[element-1]:
                c += 1
    return c

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

	
#2

print(count_isolated([1, 2, 3, 4, 5]))

	

#5