class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        complete = defaultdict(int)
        count = 0
        
        left =0
        for right ,num in enumerate(nums):
            complete[num] += 1
            while len(complete) == distinct:
                count += len(nums)-right
                complete[nums[left]] -= 1
                if complete[nums[left]] == 0:
                    complete.pop(nums[left])
                left += 1

        return count