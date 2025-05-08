'''An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists
 of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
If the second input is not '+' or '-', again raise a FormulaError.
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.'''

class FormulaError(Exception):
    """Input errors"""

def calculate(operation: str):
    
    parts = operation.split()
    if len(parts) != 3:
        raise FormulaError("Need 3 elements")
     
    try:
        a = float(parts[0])
    except ValueError:
        raise FormulaError("Need a valid number")
    
    op = parts[1]
    if op not in ("+", "-"):
        raise FormulaError("Operator has to be either '+' or '-'")
    
    try:
        b = float(parts[2])        
    except ValueError:
        raise FormulaError("Need a valid number")
    
    if op == "-":
        return a - b
    else:
        return a + b
    
while True:   
    
    word: str = input("Type the operation or 'quit': ").lower()

    if word == "quit":
        break    

    try:
        print(calculate(word))
    
    except FormulaError as x:
        print("Error:", x)

import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate("2 + 3"), 5.0)

    def test_sub(self):
        self.assertEqual(calculate("10 - 4"), 6.0)

    def test_spaces(self):
        self.assertEqual(calculate("   7    +    8 "), 15.0)

    def test_negative_num(self):
        self.assertEqual(calculate("-5 - -3"), -2.0)

    def test_float(self):
        self.assertEqual(calculate("3.5 + 2.5"), 6.0)

    def test_invalid(self):
        self.assertIsNone(calculate("2 * 3")) 

    def test_non_num(self):
        self.assertIsNone(calculate("fpuzz + 3"))

    def test_missing_elements(self):
        self.assertIsNone(calculate("2 +"))  

    def test_extra_elements(self):
        self.assertIsNone(calculate("2 + 3 + 4"))

    def test_empty(self):
        self.assertIsNone(calculate("     "))  

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))



