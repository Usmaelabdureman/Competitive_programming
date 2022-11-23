#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for _ in range(1,n):
        temp=arr[_]
        j=_-1
        while (arr[j]>temp and j>=0):
            arr[j+1]=arr[j]
            j-=1
            
        arr[j]=temp
        print(arr)
        
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

