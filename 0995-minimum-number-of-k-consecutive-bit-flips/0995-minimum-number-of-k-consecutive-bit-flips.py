class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Keeps track of flipped states
        flipped = [False] * len(nums)

        # Tracks valid flips within the past window
        validFlipsFromPastWindow = 0

        # Counts total flips needed
        flipCount = 0

        for i in range(len(nums)):
            if i >= k:
                # Decrease count of valid flips from the past window if needed
                if flipped[i - k]:
                    validFlipsFromPastWindow -= 1

            # Check if current bit needs to be flipped
            if validFlipsFromPastWindow % 2 == nums[i]:
                # If flipping the window extends beyond the array length,
                # return -1
                if i + k > len(nums):
                    return -1

                # Increment the count of valid flips and
                # mark current as flipped
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1

        return flipCount