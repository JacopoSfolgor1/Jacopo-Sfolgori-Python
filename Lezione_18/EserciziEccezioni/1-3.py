'''3-Context Managers for File Handling:
 Use the with statement and context managers to open and close a file. 
 Handle potential IOError within the with block for clean resource management.'''

try:
    with open("non.esisto") as file:
        readme = file.read()
except IOError as error:
    print(error)
