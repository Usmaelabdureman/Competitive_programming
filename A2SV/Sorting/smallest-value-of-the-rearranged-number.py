from functools import cmp_to_key

class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = [str(val) for val in str(num)]

        def compare(x, y):
            if x + y > y + x:
                return 1
            else:
                return -1
        if nums[0] == '-':
            ans = sorted(nums, key=cmp_to_key(compare), reverse=True)
            ans = -int(''.join(ans[:-1]))
        else:
            # Handle positive numbers with the first digit as zero
            ans = sorted(nums, key=cmp_to_key(compare))
            non_zero_index = next((i for i, digit in enumerate(ans) if digit != '0'), -1)
            if non_zero_index!=-1:
                ans[0],ans[non_zero_index]=ans[non_zero_index],ans[0]
            ans=int(''.join(ans))
        return ans
