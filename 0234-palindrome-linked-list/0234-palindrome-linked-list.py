# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):

        slow_ptr = head
        fast_ptr = head
        midnode = None

        #Here the idea is to get the middle of linked list

        while fast_ptr and fast_ptr.next:
           slow_ptr,fast_ptr=slow_ptr.next,fast_ptr.next.next
        midnode =slow_ptr
        slow_ptr=slow_ptr.next
        midnode.next=None #to check for odd list

        #Now reverse the second half of linked list
        while slow_ptr:
            slow_ptr.next,midnode,slow_ptr=midnode,slow_ptr,slow_ptr.next
        fast_ptr=head
        slow_ptr=midnode

        #compare the first half and reverse of the second half
        while slow_ptr:
            if fast_ptr.val!=slow_ptr.val:return False
            fast_ptr,slow_ptr= fast_ptr.next,slow_ptr.next
        return True