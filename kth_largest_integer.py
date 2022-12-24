class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        s=sorted([int(i) for i in nums],reverse=True)
        return str(s[k-1])


        