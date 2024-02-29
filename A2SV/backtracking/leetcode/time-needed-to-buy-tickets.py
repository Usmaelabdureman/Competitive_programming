class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque()
        cnt = 0

        for indx,ticket in enumerate(tickets):
            if indx <= k:
                cnt += min(ticket,tickets[k])
            else:
                cnt += min(ticket,tickets[k]-1)
        return cnt