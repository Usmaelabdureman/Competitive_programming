class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        prev=1
        for i in range(1, rowIndex+1):
            nextVal=prev*(rowIndex-i +1)//i
            ans.append(nextVal)
            prev=nextVal
        return ans
    
        