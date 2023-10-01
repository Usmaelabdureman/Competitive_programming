class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first =edges[0]
        second=edges[1]
        center =set(first) & set(second)
        return center.pop()