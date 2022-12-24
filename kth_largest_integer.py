class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        s=[int(i) for i in nums]
    
        output=sorted(s,reverse=True)
        return str(output[k-1])





        