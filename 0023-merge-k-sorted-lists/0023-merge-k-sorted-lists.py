# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push the first node from each list into the min_heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i))
                lists[i] = lists[i].next  # Move to the next node
        
        dummy = ListNode()  # Dummy node for the merged list
        current = dummy
        
        # Continue until the heap is empty
        while min_heap:
            val, index = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))
                lists[index] = lists[index].next
                
        return dummy.next