class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]

        # Fill the prefix_max array
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])

        # Fill the suffix_min array in reverse order
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])

        chunks = 0
        for i in range(n):
            # A new chunk can be created
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1

        return chunks