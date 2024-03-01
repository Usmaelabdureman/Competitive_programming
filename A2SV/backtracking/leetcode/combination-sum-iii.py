class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        high = 9

        def backtrack(indx = 1, path = []):
            if sum(path) == n and len(path) == k:
                result.append(path[:])
                return
            
            for i in range(indx, high + 1):
                if i + sum(path) <= n:
                    path.append(i)
                    backtrack(i + 1,path)
                    path.pop()
        result = []
        backtrack()
        return result