class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict=defaultdict(int)
        for num in nums:
            nums_dict[num]+=1
        res=sorted(nums_dict.items(),key=lambda value:value[1],reverse=True)
        return [res[i][0] for i in range(k)]