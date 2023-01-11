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
        if head == None:
            return None
        if head.next == None:
            return head
        else:
            temp = self.reverseList(head.next)
            if(temp != None):
                current = temp
                while(temp.next != None):
                    temp = temp.next
                head.next = temp.next
                temp.next = head
        return current