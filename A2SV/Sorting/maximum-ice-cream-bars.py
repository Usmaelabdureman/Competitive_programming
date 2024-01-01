class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for cost in costs:
            if cost<=coins:
                ans+=1
                coins-=cost
            else:
                break
        return ans

        # with counting sort but slow runtime 
        # min_cost = min(costs)
        # max_cost = max(costs)
        
        # count = [0] * (max_cost - min_cost + 1)
        
        # for cost in costs:
        #     count[cost - min_cost] += 1
        # # 
        # res = 0
        # for i in range(len(count)):
        #     if coins >= i + min_cost and count[i] > 0:
        #         num_bought = min(count[i], coins // (i + min_cost))
        #         res += num_bought
        #         coins -= num_bought * (i + min_cost)
        # return res
