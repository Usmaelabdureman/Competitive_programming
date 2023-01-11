# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        current = head
        while current:
            new_data = current.next # new_date
            current.next = new_list 
            new_list = current # new_list = {val=2, next=ListNode{1, None}
            current = new_data # current = None
        return new_list