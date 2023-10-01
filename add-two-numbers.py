class Solution:
    def addTwoNumbers(self, l1, l2 ,d = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + d
        d = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or d != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,d)
        return ret 