def print_rangoli(size):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    max_len = size * 4 - 3
    n = size
    rows = []
    
    for i in range(n): 
        
        left = [alphabet[size - 1 - j] for j in range(i + 1)]
        
        right = left[::-1][1:]
        
        full_row = left + right
        
        row_string = '-'.join(full_row)
        
        rows.append(row_string.center(max_len, '-'))
    
    for row in rows:
        print(row)

    for row in reversed(rows[:-1]):
        print(row)
        
for n in range(1, 26 + 1):
    print(f"Rangoli for size {n}:")
    print_rangoli(n)
    print("\n" + "="*50 + "\n")