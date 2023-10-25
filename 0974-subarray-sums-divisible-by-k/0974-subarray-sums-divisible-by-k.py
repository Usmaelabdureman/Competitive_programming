class Solution:
    def subarraysDivByK(self, nums, k):
        n = len(nums)
        prefixMod = 0
        result = 0

        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            # Take modulo twice to avoid negative remainders.
            prefixMod = (prefixMod + num % k + k) % k
            # Add the count of subarrays that have the same remainder as the current
            # one to cancel out the remainders.
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        return result

        
        
        