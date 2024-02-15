class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        ans_arr = arr.copy()
        ans_arr.sort()
        if ans_arr[0] != 1:
            ans_arr[0] = 1
    
        for i in range(1,n):
            diff = ans_arr[i] - ans_arr[i-1]
            if diff <= 1:
                continue
            else:
                ans_arr[i] = ans_arr[i-1] + 1
        return ans_arr[-1]

