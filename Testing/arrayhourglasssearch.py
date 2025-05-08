'''Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (

) is:

2 4 4
  2
1 2 4
'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxglass = float("-inf")
    
    for i in range(1,5):
        for i2 in range(1,5):
            
            top = arr[i-1][i2-1] + arr[i-1][i2] + arr[i-1][i2+1]
            
            mid = arr[i][i2]
            
            bottom = arr[i+1][i2-1] + arr[i+1][i2] + arr[i+1][i2+1]
            
            glass = top + mid + bottom 
            
            maxglass = max(maxglass,glass)

    print(maxglass)    