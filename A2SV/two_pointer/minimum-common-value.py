class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Bruteforce =>TLE
        # common_min=[]
        # num1_pointer=0
        # num2_pointer=0
        # for num in nums1:
        #     if num in nums2:
        #         common_min.append(num)
        # return min(common_min) if common_min else -1
        num1_pointer=0
        num2_pointer=0
        common_min=float('inf')
        while num1_pointer < len(nums1) and num2_pointer<len(nums2):
            if nums1[num1_pointer] < nums2[num2_pointer]:
                num1_pointer+=1
            elif nums1[num1_pointer] > nums2[num2_pointer]:
                num2_pointer+=1
            else:
                common_min=min(common_min,nums1[num1_pointer])
                break
        return -1 if common_min == float('inf') else common_min



