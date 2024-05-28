from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.component_count = n  # initially, count is the number of nodes

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
        if rootU == rootV:
            return False
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootV] > self.rank[rootU]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootU] = rootV
            self.rank[rootV] += 1
        self.component_count -= 1  # decrement the number of components after a union
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF, bobUF = UnionFind(n), UnionFind(n)
        edgesToRemove = 0

        
        for edgeType, u, v in edges:
            if edgeType == 3:
                if not aliceUF.union(u - 1, v - 1):
                    edgesToRemove += 1
                else:
                    bobUF.union(u - 1, v - 1)  

        for edgeType, u, v in edges:
            if edgeType == 1:
                if not aliceUF.union(u - 1, v - 1):
                    edgesToRemove += 1
            elif edgeType == 2:
                if not bobUF.union(u - 1, v - 1):
                    edgesToRemove += 1
                    

        if aliceUF.component_count == 1 and bobUF.component_count == 1:
            return edgesToRemove
        else:
            return -1
