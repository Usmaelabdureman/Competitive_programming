class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        mydict = {}
        for i in range(len(nums2)):
            if len(mono_stack) == 0:
                mono_stack.append(nums2[i])
                continue
            if nums2[i] > mono_stack[-1]:
                while len(mono_stack) > 0 and nums2[i] > mono_stack[-1]:
                    mydict[mono_stack.pop()] = nums2[i]
            mono_stack.append(nums2[i])
        for i in mono_stack:
            mydict[i] = -1
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            ans[i] = mydict[nums1[i]]
        return ans