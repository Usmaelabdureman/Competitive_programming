class Solution:
    def __init__(self) -> None:
        self.stack=[]
        self.maxStack=[]
    def push(self,val):
        self.stack.append(val)
        val=max(val,self.maxStack[-1] if self.maxStack else val)
        self.maxStack(val)
    def pop(self):
        self.stack.pop()
        self.maxStack.pop()
    def top(self)->int:
        return self.stack[-1]
    def getMax(self)->int:
        return self.maxStack[-1]

def main():
    sol=Solution()
    arr=[[],[-2],[0],[-3],[],[],[],[]]
    for i in arr:
        sol.push(i)
        
    print(sol.getMax())

if __name__ == '__main__':
    main()

    
