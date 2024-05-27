class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            point, brainpower = questions[i]
            return max(point + dfs(i + brainpower + 1), dfs(i + 1))

        return dfs(0)
