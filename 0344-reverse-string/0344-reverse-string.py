class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left=0
        # right=len(s)-1
        # while left<=right:
        #     s[left],s[right]=s[right],s[left]
        #     left+=1
        #     right-=1

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]

                helper(left + 1, right - 1)

        helper(0, len(s) - 1)