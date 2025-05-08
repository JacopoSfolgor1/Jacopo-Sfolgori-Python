'''SAMPLE INPUT:
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

SAMPLE OUTPUT:
AB
CA
AD'''

def merge_the_tools(string, k):
    # your code goes here
    
    s = [string[i:i+k] for i in range(0, len(string), k)]

    for i in s:
        chars = ""
        for char in i:
            if char not in chars:
                chars += char
        print(chars)
    
    
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)