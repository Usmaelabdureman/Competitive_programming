class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def canPlace(x,pos,m):
            prev_ball_pos = pos[0]
            balls_placed = 1
            
            for i in range(1,len(pos)):
                curr_pos = pos[i]
                if curr_pos - prev_ball_pos >= x:
                    balls_placed += 1
                    prev_ball_pos = curr_pos
                if balls_placed == m:
                    return True
            return False

        
        n = len(position)
        position.sort()

        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if canPlace(mid, position, m):

                low = mid + 1
            else:

                high = mid - 1
                
        return low - 1