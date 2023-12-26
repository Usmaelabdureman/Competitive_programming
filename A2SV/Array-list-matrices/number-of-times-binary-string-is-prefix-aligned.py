class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        aligned_count = 0
        max_index = 0

        for i, index in enumerate(flips):
            max_index = max(max_index, index)

            if max_index == i + 1:  # Check if the maximum index flipped equals the current position
                aligned_count += 1

        return aligned_count