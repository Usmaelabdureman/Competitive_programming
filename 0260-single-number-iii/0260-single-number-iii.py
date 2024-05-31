class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor_of_2num = 0
        
        for num in nums:
            xor_of_2num ^=num
            
        RMB = xor_of_2num & -xor_of_2num
        
        # print(RMB)
        
        num1,num2 = 0,0
        
        for num in nums:
            
            if num & RMB :
                num1 ^= num
            else:
                num2 ^= num
        return [num1,num2]