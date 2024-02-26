class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result 