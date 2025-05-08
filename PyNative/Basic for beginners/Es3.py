'''Exercise 3: Print characters present at an even index number

Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display 'P', 'n', 't', 'v'.'''

word: str = str(input("Inserisci la parola da scomporre: "))


for i in range(0, len(word), 2):
    print(word[i])
