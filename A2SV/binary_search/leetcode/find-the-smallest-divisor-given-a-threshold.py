class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divisor(div):
            return sum(math.ceil(num / div) for num in nums)
        
        low = 1
        high = max(nums)
        ans=1

        while low <= high:
            mid = (low + high)//2
            # print('mid',mid)

            if divisor(mid) > threshold:
                low = mid + 1
            else:
                
                ans=mid
                high = mid - 1
        return ans
