"""
Rumor
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Vova promised himself that he would never play computer games... But recently Firestorm — a well-known game developing company — published their newest game, World of Farcraft, and it became really popular. Of course, Vova started playing it.

Now he tries to solve a quest. The task is to come to a settlement named Overcity and spread a rumor in it.

Vova knows that there are n characters in Overcity. Some characters are friends to each other, and they share information they got. Also Vova knows that he can bribe each character so he or she starts spreading the rumor; i-th character wants ci gold in exchange for spreading the rumor. When a character hears the rumor, he tells it to all his friends, and they start spreading the rumor to their friends (for free), and so on.

The quest is finished when all n characters know the rumor. What is the minimum amount of gold Vova needs to spend in order to finish the quest?

Take a look at the notes if you think you haven't understood the problem completely.

Input
The first line contains two integer numbers n and m (1 ≤ n ≤ 105, 0 ≤ m ≤ 105) — the number of characters in Overcity and the number of pairs of friends.

The second line contains n integer numbers ci (0 ≤ ci ≤ 109) — the amount of gold i-th character asks to start spreading the rumor.

Then m lines follow, each containing a pair of numbers (xi, yi) which represent that characters xi and yi are friends (1 ≤ xi, yi ≤ n, xi ≠ yi). It is guaranteed that each pair is listed at most once.

Output
Print one number — the minimum amount of gold Vova has to spend in order to finish the quest.

Examples
inputCopy
5 2
2 5 3 4 8
1 4
4 5
outputCopy
10
inputCopy
10 0
1 2 3 4 5 6 7 8 9 10
outputCopy
55
inputCopy
10 5
1 6 2 7 3 8 4 9 5 10
1 2
3 4
5 6
7 8
9 10
outputCopy
15
Note
In the first example the best decision is to bribe the first character (he will spread the rumor to fourth character, and the fourth one will spread it to fifth). Also Vova has to bribe the second and the third characters, so they know the rumor.

In the second example Vova has to bribe everyone.

In the third example the optimal decision is to bribe the first, the third, the fifth, the seventh and the ninth characters.


    """
from sys import stdin, stdout
from collections import defaultdict

def dfs(v, c):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            min_cost[0] = min(min_cost[0], c[v])
            for u in graph[v]:
                if not visited[u]:
                    stack.append(u)

n, m = map(int, stdin.readline().split())
c = list(map(int, stdin.readline().split()))
c = [0] + c
graph = defaultdict(list)
visited = [False]*(n+1)
min_cost = [0]
total_cost = 0

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    if not visited[i]:
        min_cost[0] = c[i]
        dfs(i, c)
        total_cost += min_cost[0]

stdout.write(str(total_cost))