# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        size = 1
        current = head

        while current.next:
            current = current.next
            size += 1

        if k % size == 0:
            return head

        k = k % size
        
        current.next = head 
        newHead_pos = size - k

        for _ in range(newHead_pos):
            current = current.next
        new_head = current.next
        current.next = None  
        return new_head