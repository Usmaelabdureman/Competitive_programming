# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        next_node = None

        i = 0

        while i < (right - left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp
            i += 1

        prev.next.next = current
        prev.next = next_node

        return dummy.next
