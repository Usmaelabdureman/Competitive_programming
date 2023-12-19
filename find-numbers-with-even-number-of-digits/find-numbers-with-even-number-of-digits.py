class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def count_digits(num):
            digit_count = 0
            while num != 0:
                num //= 10
                digit_count += 1
            return digit_count
        
        cnt=0
        for num in nums:
            if count_digits(num) %2 == 0:
                cnt+=1
        return cnt