'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.'''

fav_numbers : dict = {"Federico" : [27, 2425], "Riccardo" : [901, 5], "Jacopo" : [56, 4], "Giovanni" : [108, 1042], "Giorgio" : [1,11]}

for key, value in fav_numbers.items():
    print(f"{key} fav numbers are: ", end = "")
    print(*value)
    