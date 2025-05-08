n = input("inserisci numero e multiplo di numero:  ")
m = n.split()
n1 = int(m[0])
n2 = int(m[1])
x  = 1


for i in range(n1):
    
    if i < n1 // 2:
        print((".|."*x).center(n2, '-'))
        x += 2
    
    if i == n1 // 2:
        print("WELCOME".center(n2, '-'))
    
    if i > n1 // 2:
        x -= 2
        print((".|."*x).center(n2,'-'))

        