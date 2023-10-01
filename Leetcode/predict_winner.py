class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.can_win = True
        def helper(left, r, ply1_turn):
            if left == r+1: # if i > r then the leftist has been traversed
                return 0
            if ply1_turn:
                return max(nums[left] + helper(left+1, r, not ply1_turn), nums[r] + helper(left, r-1, not ply1_turn))
            else:
                return min(helper(left+1, r, not ply1_turn), helper(left, r-1, not ply1_turn))
            
        score1 = helper(0, len(nums)-1, True)
        score2 = sum(nums) - score1
        
        return score1 >= score2