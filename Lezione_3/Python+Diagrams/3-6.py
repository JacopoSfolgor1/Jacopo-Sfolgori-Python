'''6. Somma condizionata di numeri in base a un valore x

Progettare un algoritmo che chieda all'utente di inserire un valore x positivo. Se x è negativo, 
l'algoritmo mostra un messaggio di errore e termina. Se x  è positivo, il programma deve consentire 
all'utente di inserire 10 numeri sia positivi che negativi. 

    Se x è pari, allora dei numeri inseriti devono essere sommati solamente i numeri che sono maggiori della metà di x. 
    Se, invece, x è dispari, dei numeri inseriti devono essere sommati solo i numeri che sono minori di x.'''

x:int = int(input("inserisci numero: "))
sum_n:int = 0

if x > 0:
    i = 0
    for i in range(10+1):
        n:int = int(input("inserisci numero: "))
        if n % 2 == 0:
            if n > x / 2:
                sum_n += n
        else:
            if n < x:
                sum_n += n
    print(sum_n)
else:
    print("x deve essere positivo e non negativo")