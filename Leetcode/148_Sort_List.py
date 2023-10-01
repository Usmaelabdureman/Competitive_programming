# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #split the list into two halfs.
        def GetMiddle(head):
            slow,fast =head,head.next
            while fast and fast.next:
                slow,fast=slow.next,fast.next.next
            return slow
        left=head
        right=GetMiddle(head)
        tmp=right.next
        right.next=None
        right=tmp

        left=self.sortList(left)
        right=self.sortList(right)
          
        def merge(leftHalf,rightHalf):
            tail=dummy=ListNode() #to avoid edge case
            while leftHalf and rightHalf:
                if leftHalf.val<rightHalf.val:
                    tail.next=leftHalf
                    leftHalf=leftHalf.next
                else:
                    tail.next=rightHalf
                    rightHalf=rightHalf.next
                tail=tail.next

            if leftHalf:
                tail.next=leftHalf
            if rightHalf:
                tail.next=rightHalf
            return dummy.next
        return merge(left,right)

     
