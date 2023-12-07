class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[] # initialize answer with empty array
        maxCandies=max(candies) 
        for i in range(len(candies)):
            ans.append(candies[i]+extraCandies>=maxCandies)
        return ans
       

     
        