class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        length=len(nums)
        for key,value in nums_dict.items():
            if value>length//2:
                return key