'''Exercise 6: Display numbers divisible by 5

Write a Python code to display numbers from a list divisible by 5'''


list_n: list = []
seq:int = int(input("inserisci quanti numeri vuoi in lista: "))


while seq > 0:
    n:int = int(input("inserisci numero: "))
    list_n.append(n)
    seq -= 1

for n in list_n:
    if n % 5 == 0:
        print(n)
    