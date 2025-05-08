'''7. Algoritmo per il calcolo della media dei voti con inserimento iterativo

Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, calcolandone la media. 
L'algoritmo deve chiedere all'utente se vuole inserire un voto. 

Se la risposta è "SI", allora l'utente può procedere ad inserire il voto. L'algoritmo deve consentire all'utente di inserire 
voti fin quando la risposta dell'utente sarà "NO". 

Infine, mostrare in output il valore medio dei voti inseriti.'''

cont:int = 0
sum_n:int = 0

word:str = input("vuoi inserire il voto? ").lower()

while word == "si":
    voto:int = int(input("inserisci voto: "))
    if voto > 0:
        cont += 1 
        sum_n += voto
    else:
        print("valore non accettato")
    word:str = input("vuoi inserire un altro voto? ").lower()
else:
    if word == "no":
        if cont > 0:
            media = sum_n / cont
            print(media)
        else:
            print("nessun voto inserito")

