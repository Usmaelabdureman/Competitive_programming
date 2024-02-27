class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(candidate,path):
            # base case
          
            if len(path) == k:
                result.append(path[:])
                return 
            
            for choice in range(candidate , n+1):
                path.append(choice)
                backtrack(choice +1,path)
                path.pop()

        result = []
        backtrack(1, [])
        return result
