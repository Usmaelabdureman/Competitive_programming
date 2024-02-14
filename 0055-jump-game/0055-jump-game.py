class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i,numJump in enumerate(nums):
            jump = max(jump, i+numJump)
            
            if jump >= len(nums)-1:
                return True
            if jump == i and numJump == 0:
                return False
        return True