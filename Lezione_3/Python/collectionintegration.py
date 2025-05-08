firstset: set[int] = {1, 5, 7, 8}
secondset: set[int] = {2, 3, 7, 6}

firstset.update(secondset) #adds 1 with +2  sets without .union() that creates a different set
print(f"{firstset}, \n{secondset}")

thirdset: set[int] = firstset.union(secondset) 
print(thirdset)

for value in firstset:
    print(value)

myset={1, "Hello", 3, 0.5, True, False,2}
print(myset) #gives it back ordered # 1 == True sets accept no duplicates also removes 1 ' ' from hello because it's a short 1 word

myset={True, "Hello how are you ", 3, 0.5, 1, False,2} #if you write true or 1 1st it prints either 1 or true based on the order you sent em
print(myset)

myset={1, "Hello", 3, 0.5, False,2} #if set not int 1 read as 1 not True and also in output False goes elsewhere and not as 0
print(myset)

dtry: dict = {"key1" : "value1", "key2" : "value2"}

for key in dtry:
    print(key) #print keys


for key in dtry:
    print(dtry[key]) #print values


for keys, values in dtry.items():
    print(f"{keys}: chiave, {values}: value") #print both


firstlst: list = [1, 2, 3, 4, 5, 6]
firstlst.extend({"key": "value", "Bool": True} ) #adds only keys as tupla from dict
firstlst.extend({"key" : "value", "Bool" : True}.items()) # adds keys and value as tupla from dict
print(firstlst) #adds 

mydict: dict[str, int] = {"a": 5, "b": 2} 

for key, value in mydict.items():
    print(key, value) 

for value in mydict.values():
    print(value)

for key in mydict.keys():
    print(key)