class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_distance = abs(target[0] - 0) + abs(target[1] - 0)
        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance <= my_distance:
                return False
        return True



        