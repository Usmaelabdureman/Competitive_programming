# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []

        curr = head
        size = 0

        while curr:
            curr = curr.next
            size += 1
        part_size = size // k
        extra = size % k

        curr = head
        for i in range(k):
            curr_size = part_size + (1 if i < extra else 0)

            new_head = curr
            for _ in range(curr_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                curr.next, curr = None, curr.next

            ans.append(new_head)

        return ans
