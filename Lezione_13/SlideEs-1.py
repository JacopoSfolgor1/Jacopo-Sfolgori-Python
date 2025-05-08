'''Write a Python function called countdown that takes a positive integer n as input and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop and the parameter n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5.'''

def countdown(n:int) -> None:
    
    if n < 0:
        print(f"{n} number is negative")

    while n >= 0:
        print(n)
        n -= 1  #non ricorsione rispetto a come fatta dopo


countdown(-5)

countdown(5)

#ricursione metodo: 

def countdown(n:int )-> None:
    
    if n < 0:       
        print("errore")

    elif n == 0: #ferma ricursione
        print(n)

    else:           
        print(n)
        countdown(n -1) 



countdown(5)

def countdown(n:int )-> None:
    
    if n < 0:       
        print("errore")

    #senza elif n == 0 a a stampare fino a errore il print di n < 0 perché calcola senza fermarsi

    #senza anche l'if n < 0 va a stampare un while infinito senza stop
    
    else:           
        print(n)
        countdown(n -1)

countdown(5)
