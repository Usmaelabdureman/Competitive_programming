from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
        head = ListNode()
        current = head
        # print("heap",heap)
        
        while heap:
            val, i = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            node = lists[i]
            lists[i] = node.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i))
        return head.next
    

test = Solution()
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]
result = test.mergeKLists(lists)
while result:
    print(result.val)
    result = result.next
# Output: 1 1 2 3 4 4 5 6

