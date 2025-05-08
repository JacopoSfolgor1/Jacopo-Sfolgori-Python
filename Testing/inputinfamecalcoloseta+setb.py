'''Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_happiness(arr, set_A, set_B):
    
    happiness = 0

    for num in arr:
        if num in set_A:
            happiness += 1  
        elif num in set_B:
            happiness -= 1 
    
    return happiness

if __name__ == '__main__':
    
    n, m = map(int, input().split())  
    
    arr = list(map(int, input().split()))
    
    set_A = set(map(int, input().split()))
    
    set_B = set(map(int, input().split()))
    
    result = calculate_happiness( arr, set_A, set_B)
    
    print(result)