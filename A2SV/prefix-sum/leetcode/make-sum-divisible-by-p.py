class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target_rem = sum(nums) % p
    
        if target_rem == 0:
            return 0
        
        rem_dict = {0: -1}
        cur_rem = 0
        result = float('inf')
        
        for i, num in enumerate(nums):
            cur_rem = (cur_rem + num) % p
            comp = (cur_rem - target_rem + p) % p
            
            if comp in rem_dict:
                result = min(result, i - rem_dict[comp])

            rem_dict[cur_rem] = i
        
        return result if result < len(nums) else -1