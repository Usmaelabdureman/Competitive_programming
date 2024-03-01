class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        
        def backtrack(indx = 0, path = []):
            if sum(path) == target:
                result.append(path[:])
                return
            # Pruning 
            if sum(path) > target or indx >= n:
                return
            
            for i in range(indx, n):
                if candidates[i] + sum(path) <= target:
                    path.append(candidates[i])
                    backtrack(i,path)
                    path.pop()
        result = []
        backtrack()
        return result