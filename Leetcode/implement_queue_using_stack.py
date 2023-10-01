class MyQueue:

    def __init__(self):
        self.S1=[]
        self.queue=[]
        
    def push(self, x: int) -> None:
        while self.S1:
            deque=self.S1.pop()
            self.queue.append(deque)
        self.S1.append(x)
        while self.queue:
            self.S1.append(self.queue.pop())
    def pop(self) -> int:
        return self.S1.pop()
    def peek(self) -> int:
        return self.S1[-1]
        
    def empty(self) -> bool:
        return not self.S1