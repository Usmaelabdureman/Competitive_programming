# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        currentOdd = head
        count = 2
        node = head
        prev = node
        node = node.next
        while node is not None:
            if count % 2 == 0:
                prev = node
                node = node.next
            else:
                next = node.next
                prev.next = next
                temp = currentOdd.next
                currentOdd.next = node
                node.next = temp
                currentOdd = node
                node = next
            count += 1
        return head