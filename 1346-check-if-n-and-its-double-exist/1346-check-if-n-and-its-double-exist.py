class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        d = defaultdict(int)
        
        for i in range(len(arr)):
            if 2*arr[i]  in d or arr[i]/2 in d:
                return True
            d[arr[i]] = i
        return False