class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        rem=0
        idx=len(digits)-1
        if(True):
            while(True):

                tmp=digits[idx]+1
                digits[idx]=tmp%10
                rem=tmp//10
                idx-=1
                if rem==0 or idx <0:
                    break
    
        if idx==-1 and digits[0]==0: 
            return [1]+digits
        return digits
                
                



            
            
        
