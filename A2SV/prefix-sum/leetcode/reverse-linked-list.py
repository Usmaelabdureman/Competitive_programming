# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        rev_list = None

        while curr:
            node = curr.next
            curr.next = rev_list
            rev_list = curr
            curr = node
           
        return rev_list