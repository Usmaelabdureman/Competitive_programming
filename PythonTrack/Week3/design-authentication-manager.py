from collections import deque

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {} # Dictionary from tokenId to expiry time.
        self.token_queue = deque() # helps keep track of which tokens to expire next. 
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        expiry = currentTime + self.ttl
        self.tokens[tokenId] = expiry
        self.token_queue.append((expiry, tokenId))


    def process_expiry(self, currentTime: int) -> int:
        count = 0
        while self.token_queue and self.token_queue[0][0] <= currentTime:
            exp, tok = self.token_queue.popleft()
            del self.tokens[tok]
            count += 1
        return count

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return
        if currentTime >= self.tokens[tokenId]:
            # token is already expired. 
            # process expiry
            num_expired = self.process_expiry(currentTime)
            return
        idx = 0
        while self.token_queue[idx][1] != tokenId:
            idx += 1
        del self.token_queue[idx]
        del self.tokens[tokenId]
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.process_expiry(currentTime)
        return len(self.token_queue)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)