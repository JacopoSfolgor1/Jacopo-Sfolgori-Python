'''Funzioni, For, While, If, Elif ed Else
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''

def comb(x, y, z):
    if x is True:
        if y | z is True:
            return "Azione permessa"
    else:
        return "Azione negata"
    
def multiply(lst: list, threshold: int): 
    newlst: list = []
    for l in range(len(lst)):
        if lst[l] < threshold & type(lst[l]) == int:
            newlst.append(lst[l])
    return newlst
    


for n in range(2,15,2):
    print(n)

for n in range(1,14,3):
    print(n)

for n in range(0,31,5):
    print(reversed(n))

for n in range(5,46,10):
    print(n)