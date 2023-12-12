class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter=len(arr)//4
        for i in range(len(arr) - quarter):
            if arr[i] == arr[i+quarter]:
                return arr[i]
        return 0