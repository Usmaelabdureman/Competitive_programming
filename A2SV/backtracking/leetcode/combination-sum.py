
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(path=[]):
            # base case
            if sum(path) == target:
                result.add(tuple(sorted(path.copy())))
                return
            
            for candidate in candidates:
                if candidate + sum(path) <= target:
                    path.append(candidate)
                    # print(path)
                    backtrack(path)
                    path.pop()

        result = set()
        backtrack()
        return result
