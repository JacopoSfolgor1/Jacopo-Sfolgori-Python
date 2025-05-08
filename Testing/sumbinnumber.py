

n = int(input())  

binary = bin(n)[2:]


max_rep = max(len(i) for i in binary.split("0"))

print(max_rep) 

#sum sequence of 1 inside binary number 