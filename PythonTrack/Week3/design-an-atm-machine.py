class ATM:
    def __init__(self):
        self.ans = [20,50,100,200,500]
        self.res = [0]*5
        
    def deposit(self, banknotesCount):
        for i in range(5):
            self.res[i] += banknotesCount[i]

    def withdraw(self, amount):
        result = [0]*5
        
        for i in range(4,-1,-1):
            n = min(self.res[i],amount//self.ans[i])
            amount -= self.ans[i]*n
            result[i] += n
            
        if amount == 0:
            self.res = [self.res[i] - result[i] for i in range(5)]
            
        return result if amount == 0 else [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)