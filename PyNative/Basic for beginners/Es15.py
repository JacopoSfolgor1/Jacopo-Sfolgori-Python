'''Exercise 15: Get an int value of base raises to the power of exponent

Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

Expected output

Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:

base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
'''


def exponent(base:int, exp:int):
    result:int = 1
    if exp <= 0:
        print("exponential has to be higher than 0")
    else:
        result = base ** exp 
        print(f"{base} rasised {exp} is: {result}")
            
        

exponent(int(input("base n: ")), int(input("exp: ")))


def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
