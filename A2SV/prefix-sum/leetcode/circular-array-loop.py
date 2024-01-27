class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            seen = set()
            j = i
            prev = i
            while nums[j] * nums[i] > 0:
                j += nums[j]
                j %= n
                if j in seen:
                    if j != prev:
                        return True
                    break
                prev = j
                seen.add(j)

        return False
