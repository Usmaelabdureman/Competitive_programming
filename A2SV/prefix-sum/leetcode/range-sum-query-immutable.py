class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.pref_sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.pref_sum[left - 1] if left > 0 else 0
        rightSum = self.pref_sum[right]
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)