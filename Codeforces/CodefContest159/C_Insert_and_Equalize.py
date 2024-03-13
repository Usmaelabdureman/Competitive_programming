"""
You are given an integer array a1,a2,…,an
, all its elements are distinct.

First, you are asked to insert one more integer an+1
 into this array. an+1
 should not be equal to any of a1,a2,…,an
.

Then, you will have to make all elements of the array equal. At the start, you choose a positive integer x
 (x>0
). In one operation, you add x
 to exactly one element of the array. Note that x
 is the same for all operations.

What's the smallest number of operations it can take you to make all elements equal, after you choose an+1
 and x
?
The number x has to be a positive (greater than 0) integer.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of testcases.

The first line of each testcase contains a single integer n
 (1≤n≤2⋅105
).

The second line contains n
 integers a1,a2,…,an
 (−109≤ai≤109
). All ai
 are distinct.

The sum of n
 over all testcases doesn't exceed 2⋅105
.

Output
For each testcase, print a single integer — the smallest number of operations it can take you to make all elements equal, after you choose integers an+1
 and x
.

Example
inputCopy
3
3
1 2 3
5
1 -19 17 -3 -15
1
10
outputCopy
6
27
1
Note
In the first testcase, you can choose an+1=4
, the array becomes [1,2,3,4]
. Then choose x=1
 and apply the operation 3
 times to the first element, 2
 times to the second element, 1
 time to the third element and 0
 times to the fourth element.

In the second testcase, you can choose an+1=13,x=4
.

In the third testcase, you can choose an+1=9,x=1
. Then apply the operation once to an+1
.

    """

# Function to solve the problem
def min_operations(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        arr = test_cases[i][1]

        # Find the minimum and maximum elements in the array
        min_val = min(arr)
        max_val = max(arr)

        # Calculate the difference between the max and min values
        difference = max_val - min_val

        # Print the number of operations required
        print(difference)

# Reading input
t = int(input())  # Number of test cases
test_cases = []
for _ in range(t):
    n = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Array elements
    test_cases.append((n, arr))

# Calling the function with inputs
min_operations(t, test_cases)
