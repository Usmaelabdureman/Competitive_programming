#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    # Write your code here
    for i in range (1,len(arr)):
        n=arr[i]
        j=i-1 #previous
        while j>=0 and arr[j]>n:
           
            arr[j+1]=arr[j]
            j-=1
            print(' '.join(str(k) for k in arr))
        arr[j+1]=n
    print(' '.join(str(k) for k in arr))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
