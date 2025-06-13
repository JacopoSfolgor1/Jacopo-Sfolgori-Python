'''Somma delle Diagonali di una Matrice (Quadrata o
Rettangolare)
Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).
Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15'''

def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    result: int = 0
    for i in range(len(matrix)):
        if i < len(matrix[i]):
            result += matrix[i][i]     
    return result

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    result: int = 0
    for i in range(len(matrix)):
        if (len(matrix[i]) - 1 - i) >= 0:
            result += matrix[i][len(matrix[i]) - 1 - i] 
    return result

mat1 = [
    [1, 2, 3],  
    [4, 5, 6], 
    [7, 8, 9]
]

mat2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

mat3 = [
    [1,2],  
    [3,4,5],
    [6,7,8,9],
    [10,11,12,13,14]
]

print(sum_primary_diagonal(mat1)) # [0][0] (1) -> [1][1] (5) -> [2][2] (9) -> 15
print(sum_secondary_diagonal(mat1)) # [0][3 - 1 - 0] (3) -> [1][3 - 1 - 1] (5) -> [2][3 - 1 - 2] (7) -> 15

print(sum_primary_diagonal(mat2)) # [0][0] (1) -> [1][1] (7) -> 8
print(sum_secondary_diagonal(mat2)) # [0][5 - 1 - 0] (5) -> [1][5 - 1 - 1] (9) -> 14  

print(sum_primary_diagonal(mat3)) # [0][0] (1) -> [1][1] (4) -> [2][2] (8) -> [3][3] (13) -> 26
print(sum_secondary_diagonal(mat3)) # [0][2 - 1 - 0] (2) -> [1][3 - 1 - 1] (4) -> [2][4 - 1 - 2] (7) -> [3][5 - 1 - 3] (11) -> 24