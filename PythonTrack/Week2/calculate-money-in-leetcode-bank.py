class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        remainder =n%7
        num_seven=n//7
        starting_point=1
        for i in range(num_seven):
            temp = starting_point
            for j in range(7):
                ans += temp
                temp += 1
            starting_point += 1
        
        for k in range(remainder):
            ans += starting_point
            starting_point += 1
        
        return ans
        
        