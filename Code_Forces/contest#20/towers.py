"""
Towers
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Little Vasya has received a young builder’s kit. The kit consists of several wooden bars, the lengths of all of them are known. The bars can be put one on the top of the other if their lengths are the same.

Vasya wants to construct the minimal number of towers from the bars. Help Vasya to use the bars in the best way possible.

Input
The first line contains an integer N (1 ≤ N ≤ 1000) — the number of bars at Vasya’s disposal. The second line contains N space-separated integers li — the lengths of the bars. All the lengths are natural numbers not exceeding 1000.

Output
In one line output two numbers — the height of the largest tower and their total number. Remember that Vasya should use all the bars.

Examples
inputCopy
3
1 2 3
outputCopy
1 3
inputCopy
4
6 5 6 7
outputCopy
2 3

    """
    
    
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
count = 1
for i in range(1, n):
    if a[i] == a[i-1]:
        count += 1
    else:
        ans.append(count)
        count = 1
ans.append(count)
print(max(ans), len(ans))

