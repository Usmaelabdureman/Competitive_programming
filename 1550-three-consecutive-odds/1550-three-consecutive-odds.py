class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        first = 0
        second = 1
        third = 2
        
        while third < len(arr):
            
            if arr[first] %2 and arr[second] %2 and arr[third] %2 :
                return True
            first +=1
            second += 1
            third +=1
        return False