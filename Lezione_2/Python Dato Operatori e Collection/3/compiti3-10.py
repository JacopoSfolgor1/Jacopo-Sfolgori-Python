'''3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, 
cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''
'''(lower, upper, title, insert, append, pop, reverse, sort, sorted, del, len)'''

languages : list = ["japanese", "italian", "english", "french", "german"] 


for i in range(len(languages)):
    print(languages[i].lower(), languages[i].upper(), languages[i].title())

languages.append("spanish")
print(languages)

languages.insert(1, "belgium")
print(languages)

languages.pop(2)
print(languages)

languages.sort()
print(languages)

languages += [4] #adds 4 in the list as last number

print(sorted(languages, reverse = True))

languages.clear() #remove items in list but not list

del languages #remove everything
print(languages)
