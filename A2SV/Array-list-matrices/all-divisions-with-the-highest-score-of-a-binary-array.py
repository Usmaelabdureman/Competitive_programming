class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        max_score = right
        indices = [0]

        for i, num in enumerate(nums):
            if num == 0:
                left += 1
            else:
                right -= 1
            
            total_score = left + right

            if max_score == total_score:
                indices.append(i + 1)
            elif max_score < total_score:
                max_score = total_score
                indices = [i + 1]

        return indices
