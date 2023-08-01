class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])  # Add a copy of the current combination to the result
                return
            
            for i in range(start, n + 1):
                path.append(i)  # Add the current number to the current combination
                backtrack(i + 1, path)  # Explore combinations starting from the next number
                path.pop()  # Backtrack by removing the last number from the current combination
        
        result = []
        backtrack(1, [])
        return result
