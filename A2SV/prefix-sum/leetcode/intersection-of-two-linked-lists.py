# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # currA = headA
        # currB = headB
        
        # while currA != currB:
            
        #     currA = currA.next if currA else headB
        #     currB = currB.next if currB else headA
        # return currA
            
        # method two using hashset

        visited = set()
        # store head A in set
        while headA:
            visited.add(headA)
            headA = headA.next
        # check if current node in visited set
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        

             