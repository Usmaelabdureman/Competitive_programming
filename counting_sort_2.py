#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.



def countingSort(arr):
    # Write your code here
    length_arr=len(arr)
    freq=[0]*100
    output=[]*100
    for i in range(length_arr):
        freq[arr[i]]+=1
    for j in range(len(freq)):
        k=freq[j]
        while k>0:
            output.append(j)
            k-=1
    return output
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
