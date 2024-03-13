class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack1 = [] 
        self.stack2 = [] 
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.stack1.append(url)
        self.stack2.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
            steps -= 1
        return self.stack1[-1]

    def forward(self, steps: int) -> str:
        while steps and self.stack2:
            self.stack1.append(self.stack2.pop())
            steps -= 1
        return self.stack1[-1]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)