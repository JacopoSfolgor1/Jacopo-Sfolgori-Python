def minion_game(string):
    kevin = "aeiou".upper()
    
    i = 0
    contk = 0
    conts = 0
    while i < len(string):
        if string[i] in kevin:
            contk += len(string) - i
        else:
            conts += len(string) - i
        i += 1
             
    if contk == conts:
        print(f"Draw: {conts}")
    else:
        if contk < conts:
            print(f"Stuart {conts}")
        else:
            print(f"Kevin {contk}")    


minion_game(input("inserisci parola: ").upper())