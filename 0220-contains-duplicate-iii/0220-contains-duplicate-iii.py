class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        if valueDiff < 0:
            return False

    
        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_index = num // bucket_size

            if bucket_index in buckets:
                return True
            if bucket_index - 1 in buckets and abs(num - buckets[bucket_index - 1]) <= valueDiff:
                return True
            if bucket_index + 1 in buckets and abs(num - buckets[bucket_index + 1]) <= valueDiff:
                return True

            buckets[bucket_index] = num

            # Remove elements outside the index difference window
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]

        return False
