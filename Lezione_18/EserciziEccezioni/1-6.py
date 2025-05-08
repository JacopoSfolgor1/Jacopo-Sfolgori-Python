'''Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:

    Create a fraction from the numerator and denominator.
    Collect the numerator and denominator of a fraction.
    Simplify a fraction.
    Add, subtract, multiply and divide fractions.
    Check whether one fraction is equivalent to another. 

    All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.

'''
class Errors(Exception):
    """Errors text"""

class Math_Library:
    
    def __init__(self):
        self.history = []
    
    def create_fraction(self, num, denom):
        try:
            num = int(num)
            denom = int(denom)
        except ValueError:
            raise Errors("Invalid input: Provide integer")
        
        if denom == 0:
            raise Errors("Invalid input: Denominator cannot be zero")
        
        simplified_num, simplified_denom = self.simplified(num, denom)
        return simplified_num, simplified_denom
    
    def simplified(self, num, denom):
        def divide(a, b):
            while b:
                a, b = b, a % b
            return a
        
        divisor = divide(num, denom)
        
        simplified_num = num // divisor
        simplified_denom = denom // divisor
        
        return simplified_num, simplified_denom
    
    def add(self, num1, denom1, num2, denom2):
        try:
            result1 = self.create_fraction(num1, denom1)
            result2 = self.create_fraction(num2, denom2)
        except Errors as x:
            raise Errors(f"Addition error: {x}")
        
        num = result1[0] * denom2 + result2[0] * denom1
        denom = denom1 * denom2
        
        simplified_num, simplified_denom = self.simplified(num, denom)
        self.history.append([simplified_num, simplified_denom])
        
        return f"{simplified_num} / {simplified_denom}"
    
    def subtract(self, num1, denom1, num2, denom2):
        try:
            result1 = self.create_fraction(num1, denom1)
            result2 = self.create_fraction(num2, denom2)
        except Errors as x:
            raise Errors(f"Subtraction error: {x}")
        
        num = result1[0] * denom2 - result2[0] * denom1
        denom = denom1 * denom2
        
        simplified_num, simplified_denom = self.simplified(num, denom)
        self.history.append([simplified_num, simplified_denom])
        
        return f"{simplified_num} / {simplified_denom}"
    
    def multiply(self, num1, denom1, num2, denom2):
        try:
            result1 = self.create_fraction(num1, denom1)
            result2 = self.create_fraction(num2, denom2)
        except Errors as x:
            raise Errors(f"Multiplication error: {x}")
        
        num = result1[0] * result2[0]
        denom = denom1 * denom2
        
        simplified_num, simplified_denom = self.simplified(num, denom)
        self.history.append([simplified_num, simplified_denom])
        
        return f"{simplified_num} / {simplified_denom}"
    
    def divide(self, num1, denom1, num2, denom2):
        try:
            result1 = self.create_fraction(num1, denom1)
            result2 = self.create_fraction(num2, denom2)
        except Errors as x:
            raise Errors(f"Division error: {x}")
        
        if result2[0] == 0:
            raise Errors("Invalid input: Cannot divide by zero")
        
        num = result1[0] * result2[1]
        denom = denom1 * result2[0]
        
        simplified_num, simplified_denom = self.simplified(num, denom)
        self.history.append([simplified_num, simplified_denom])
        
        return f"{simplified_num} / {simplified_denom}"

    def equals(self, num1, denom1, num2, denom2):
        try:
            result1 = self.create_fraction(num1, denom1)
            result2 = self.create_fraction(num2, denom2)
        except Errors as x:
            raise Errors(f"Equality check error: {x}")
        
        simplified1 = self.simplified(result1[0], result1[1])
        simplified2 = self.simplified(result2[0], result2[1])
        
        return f"{simplified1 == simplified2}, between {simplified1} and {simplified2}"

math_lib = Math_Library()

fraction1 = math_lib.create_fraction(3, 6)
fraction2 = math_lib.create_fraction(2, 5)

print("Add:", math_lib.add(3, 6, 2, 5))
print("Subtract:", math_lib.subtract(3, 6, 2, 5))
print("Multiply:", math_lib.multiply(3, 6, 2, 5))
print("Divide:", math_lib.divide(3, 6, 2, 5))
print("Equals:", math_lib.equals(3, 6, 1, 2))

print("History:", math_lib.history)

try:
    print(math_lib.create_fraction("a", 5))
except Errors as x:
    print("Error:", x)

try:
    print(math_lib.create_fraction(3, 0))
except Errors as x:
    print("Error:", x)

try:
    print(math_lib.add("a", 5, 2, 3))
except Errors as x:
    print("Error:", x)

try:
    print(math_lib.divide(3, 6, 0, 0))
except Errors as x:
    print("Error:", x)
