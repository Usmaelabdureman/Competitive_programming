class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
    
        def backtrack(indx = 0, path = []):
            if sum(path) == target:
                result.add(tuple(sorted(path[:])))
                return
            # Pruning 
            if sum(path) > target or indx >= n:
                return
            for i in range(indx, n):
                if i > indx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + sum(path) <= target:
                    path.append(candidates[i])
                    backtrack(i + 1 ,path)
                    path.pop()
        result = set()
        backtrack()
        return result