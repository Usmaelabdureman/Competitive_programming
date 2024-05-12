import sys
from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    nodes = list(map(int, input().split()))
    colors = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(2,n+1):
        graph[nodes[i-2]].append(i)
    # print(graph)
    def dfs(node, parcolor):
        nonlocal cnt
        if colors[node - 1] != parcolor:
            cnt += 1
        for neigh in graph[node]:
            dfs(neigh, colors[node  - 1])     
    cnt = 0
    dfs(1,0)
    print(cnt)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
