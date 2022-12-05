class Solution:
    def middleNode(self, head):
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
