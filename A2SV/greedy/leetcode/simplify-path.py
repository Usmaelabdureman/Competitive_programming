class Solution:
    def simplifyPath(self, path):
        stack = []
        directories = path.split("/")
       
        for dir in directories:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return "/"+ "/".join(stack)