class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0

        for start in range(len(arr) - 1):
            xor_A = 0

            # Iterate over each possible middle index j
            for mid in range(start + 1, len(arr)):
                xor_A ^= arr[mid - 1]

                xor_B = 0

                for end in range(mid, len(arr)):
                    # Update xor_B to include arr[end]
                    xor_B ^= arr[end]

                    # found a valid triplet (start, mid, end)
                    if xor_A == xor_B:
                        count += 1

        return count