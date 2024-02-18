class Solution(object):
    def deleteNode(self, node):
        size = 0
        curr = node
        
        next_node = curr.next
        curr.val = next_node.val
        
        curr.next = next_node.next
        next_node.next = None
        
        del next_node