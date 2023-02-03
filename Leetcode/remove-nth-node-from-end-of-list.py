# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while right and  n>0:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        
        #delete the node just change the pointer of the previous element to the next of deleted element
        left.next=left.next.next
        return dummy.next
        
            
        
