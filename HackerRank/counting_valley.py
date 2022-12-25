#!/bin/python3
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
def countingValleys(steps, path):
    # Write your code here
    height = 0
    no_valley = 0
    
    for i in path:
        height += 1 if i == 'U' else -1
        no_valley += 1 if height == 0 and i == 'U' else 0
    return no_valley
