class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maxSofar=arr[n-1]
        for i in range(n-1,-1,-1):
            curr_max=arr[i]
            arr[i]=maxSofar
            maxSofar=max(maxSofar,curr_max)
        arr[-1]=-1
        return arr
        
            
        