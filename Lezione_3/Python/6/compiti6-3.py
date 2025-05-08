'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

glossary: dict = {".lower": "apply to a string all lower letters", ".upper": "apply to a string all upper letters", 
             "len()" : "check how many items are in the variable", ".copy" : "creates a copy of the list that will be shallow", 
             ".clear" : "empty the values inside the variable but doesn't remove the variable itself", 
             ".sort()" : "it will modify the order of the variable based on alphabetical or numerical order "}
    
for key,value in glossary.items():
    print(f"{key}: {value}\n")