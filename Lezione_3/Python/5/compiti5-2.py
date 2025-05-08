'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

dog = "shiba"
print("Is dog == 'Setter'? I predict False.")
print(dog == 'Setter')

print("Is dog == 'Shiba'? I predict True.")
print(dog == 'Shiba')

print("Is dog.lower() == 'shiba'? I predict True.")
print(dog.lower() == 'shiba')

print("Is dog.lower() == 'Setter'? I predict False.")
print(dog.lower() == 'Setter')

print("Is dog >= 'setter'? I predict True.")
print(dog >= 'setter')

print("Is dog <= 'setter'? I predict False.")
print(dog <= 'setter')

print(f"Is {dog and 'shiba'} == \'setter\'? I predict False.") 
print(dog and 'shiba' == 'setter')

print(f"Is {dog and not 'shiba'} == \'setter\'? I predict True.") 
print(dog and not 'shiba' == 'setter')

dogs : list = ["husky", "setter", "shiba"]

print(f"if \"husky\" in {dogs} I predict True") 
print("husky" in dogs)

print(f"if \"chihuahua\" in {dogs} I predict False") 
print("chihuahua" in dogs)