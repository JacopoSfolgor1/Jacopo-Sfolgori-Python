'''Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4'''
n = int(input())  
s = set(map(int, input().split())) 

m = int(input())  

for i in range(m):
    wn = input().split()  
    word = wn[0]  
    
    if word == "pop":
        s.pop()
    
    elif word == "remove":
        value = int(wn[1])  
        s.remove(value)
    
    elif word == "discard":
        value = int(wn[1])  
        s.discard(value)

print(sum(s))


#MARCH MATCH WAY 

n = int(input())  
s = set(map(int, input().split())) 

m = int(input())  

for i in range(m):
    wn = input().split()  
    word = wn[0]  
    
    match word:
        case "pop":
            s.pop()
    
        case "remove":
            value = int(wn[1])  
            s.remove(value)
    
        case "discard":
            value = int(wn[1])  
            s.discard(value)

print(sum(s))