# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy2 = ListNode()
        Linked_List1 = dummy # to store value less than x
        Linked_List2 = dummy2   # to store value greater than or equal to x

        while head:
            if head.val < x:
                Linked_List1.next = head
                Linked_List1 = Linked_List1.next
            else:
                Linked_List2.next = head
                Linked_List2 = Linked_List2.next
            head = head.next
        print(dummy2.next)
        Linked_List1.next = dummy2.next
        Linked_List2.next = None
        return dummy.next