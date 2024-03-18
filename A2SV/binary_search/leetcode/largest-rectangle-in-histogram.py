class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        max_area = 0
        i = 0
        while i < n: 

            if  not stack or heights[ stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:

                poped = stack.pop()
                height = heights[poped]
                width = i if not stack else i - stack[-1]-1

                curr_max =width * height
                max_area = max(max_area , curr_max)
        while stack:
            poped = stack.pop()
            height = heights[poped]
            width = i if not stack else i - stack[-1]-1
            curr_max =width * height
            max_area = max(max_area , curr_max)
        return max_area
