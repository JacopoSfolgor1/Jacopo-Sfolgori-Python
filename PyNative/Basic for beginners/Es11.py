'''Exercise 11: Get each digit from a number in the reverse order.

For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.'''

n:str = (input("inserisci numero: "))

n_str:str = n[::-1]


for n in n_str:
    print(n, end = " ")