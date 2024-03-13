class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = sorted(a + b for a, b in pairwise(weights))
        
        sum_of_largest_k = sum(arr[len(arr) - k + 1 :])
        sum_of_less_k_minus_1 = sum(arr[: k - 1])

        return sum_of_largest_k - sum_of_less_k_minus_1
