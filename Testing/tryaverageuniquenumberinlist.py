def average(array):
    # your code goes here
    arr = list(set(array))
    
    sum_tot = sum(arr)
    avg = sum_tot / len(arr)
    return avg 
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)