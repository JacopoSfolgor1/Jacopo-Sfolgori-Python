'''Exercise 9: Check Palindrome Number

Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. 
For example, 545 is the palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number'''

n:str= input("inserisci numero: ")
n_rev: int = int(n[::-1])
n_int: int = int(n)

if n_int == n_rev:
    print(f"{n_int} is palindrome")
else:
    print(f"{n_int} not")