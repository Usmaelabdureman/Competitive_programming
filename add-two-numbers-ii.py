# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ListToStack(head):
            stack=[]
            while head:
                stack.append(head.val)
                head=head.next
            return stack
        stack1=ListToStack(l1)
        stack2=ListToStack(l2)
        current=None
        carry=0
        while stack1 or stack2 or carry:
            Sum=carry
            Sum+=stack1.pop() if stack1 else 0
            Sum+=stack2.pop() if stack2 else 0
            dummy=ListNode(Sum%10)
            dummy.next=current
            current=dummy
            carry=Sum//10
        return current
    