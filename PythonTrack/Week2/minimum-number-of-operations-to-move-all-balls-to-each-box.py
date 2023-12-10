class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return list(map(lambda i: sum(abs(i - j) for j in range(len(boxes)) if boxes[j] == '1'), range(len(boxes))))
