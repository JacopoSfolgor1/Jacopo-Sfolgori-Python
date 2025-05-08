n_players = int(input("Please state how many players: "))

for n in range(1, n_players +1):
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n== 3:
        print(f"{n}rd")
    else: 
        print(f"{n}th")
    n_players -= 1


'''match: n #variable n already given
#n = 1
case 1:
    print("1st")
#n = 2
case 2:
    print("2nd")
#n = 3
case 3:
    print("3rd")
#default case
case _:
    print(f"{n}th")'''