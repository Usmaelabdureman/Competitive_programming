class RecentCounter:

    def __init__(self):
        self.stack = []
        self.min = 0

    def ping(self, t: int) -> int:
        self.stack.append(t)
        lenOfStack = len(self.stack)
        rangedTo = t-3000
        if rangedTo <= 0:
            return lenOfStack
        
        for i in range(self.min, len(self.stack)):
            if self.stack[i] >= rangedTo:
                self.min = i
                return lenOfStack - i