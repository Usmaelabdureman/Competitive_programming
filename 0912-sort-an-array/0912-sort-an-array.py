class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        mid = len(nums)//2

        def merge(left_half,right_half) -> List[int]:
            merged = []
            l1, l2 = 0, 0
            r1, r2 = len(left_half), len(right_half)
            
            while l1 < r1 and l2 < r2:
                if left_half[l1] < right_half[l2]:
                    merged.append(left_half[l1])
                    l1 += 1
                else:
                    merged.append(right_half[l2])
                    l2 += 1
            
            while l1 < r1:
                merged.append(left_half[l1])
                l1 += 1
            
            while l2 < r2:
                merged.append(right_half[l2])
                l2 += 1
            return merged

        if len(nums) == 1:
            return nums
            
        left_part = self.sortArray(nums[:mid])
        right_part = self.sortArray(nums[mid:])

        return merge(left_part,right_part)
        
