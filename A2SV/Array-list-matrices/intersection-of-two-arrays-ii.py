class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1_freq = defaultdict(int)
        # for num in nums1:
        #     num1_freq[num] += 1

        # k = 0
        # for num in nums2:
        #     cnt = num1_freq.get(num, 0)
        #     if cnt > 0:
        #         nums1[k] = num
        #         k += 1
        #         num1_freq[num] = cnt - 1
        # return nums1[:k]
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                k += 1
                i += 1
                j += 1
        return nums1[:k]