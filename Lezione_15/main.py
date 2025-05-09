'''PATH: str = "Lezione_15/test.txt"
mode: str = "w"
econding: str = "utf-8"

file = open(PATH, mode)
message: str = "FPUZZ"
output: str = file.write(message)

print(output)
file.close()'''

with open("Lezione_15/test.txt","r") as file:
    print(file.read())

