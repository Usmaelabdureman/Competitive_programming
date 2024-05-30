class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0

        # Iterate over each possible starting index i
        for start in range(len(arr) - 1):
            # Initialize XOR value for the subarray from start to mid-1
            xor_A = 0

            # Iterate over each possible middle index j
            for mid in range(start + 1, len(arr)):
                # Update xor_A to include arr[mid - 1]
                xor_A ^= arr[mid - 1]

                # Initialize XOR value for the subarray from mid to end
                xor_B = 0

                # Iterate over each possible ending index k (starting from mid)
                for end in range(mid, len(arr)):
                    # Update xor_B to include arr[end]
                    xor_B ^= arr[end]

                    # found a valid triplet (start, mid, end)
                    if xor_A == xor_B:
                        count += 1

        return count