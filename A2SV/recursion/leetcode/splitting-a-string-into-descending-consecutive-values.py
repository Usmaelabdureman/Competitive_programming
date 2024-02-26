class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(i,prev):
            if i == n:
                return True
                
            valid = False
            for indx in range(i+1,n+1):
                if int(s[i:indx]) == prev - 1:
                    valid = valid or  backtrack(indx,prev - 1)
                if valid:
                    return True
            return valid
        

        for i in range(1,n):
            if  backtrack(i,int(s[:i])):
                return True
        return False
