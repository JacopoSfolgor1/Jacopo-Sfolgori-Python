'''Exercise 5: Check if the first and last numbers of a list are the same

Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.'''


list_n: list = []
seq:int = int(input("inserisci quanti numeri vuoi in lista: "))
check: bool = False

while seq > 0:
    n:int = int(input("inserisci numero: "))
    list_n.append(n)
    seq -= 1

for n in list_n:
    if list_n[0] == list_n[-1]:
        check = True
    else:
        check = False

print(f"sono primo ed ultimo numero uguali? \n{check}")