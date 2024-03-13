class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) < 1:
            return []

        digToChar={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

        def backtrack(i = 0,subs = "" ):

            if len(subs) == len(digits):
                result.append(subs)
                return 
            
            for choice in digToChar[digits[i]]:
                # subs + choice
                backtrack(i+1,subs + choice)
                # subs.remove(subs[-1])
                
        result = []
        backtrack()
        return result