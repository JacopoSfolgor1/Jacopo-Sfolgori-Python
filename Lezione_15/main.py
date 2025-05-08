PATH: str = "Lezione_15/test.txt"
mode: str = "r"
econding: str = "utf-8"

file = open(PATH)

output: str = file.read()

print(output)