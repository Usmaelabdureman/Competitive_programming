class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        
    def pop(self) -> int:
        # Move elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        # Pop the last element from q1 (which is the top of the stack)
        popped_element = self.q1.pop(0)
        
        # Swap q1 and q2 for future operations
        self.q1, self.q2 = self.q2, self.q1
        return popped_element
        
    def top(self) -> int:
        # Move elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        # Get the last element from q1 (which is the top of the stack)
        top_element = self.q1[0]
        
        # Move the elements back to q1
        self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        return top_element
        
    def empty(self) -> bool:
        return len(self.q1) == 0

