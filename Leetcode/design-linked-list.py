class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
    
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr=self.getNode(index)
        return -1 if curr==None else curr.val

    def getNode(self,index):
            i=0
            cur=self.head
            while (i<index and cur!=None):
                cur=cur.next
                i+=1
            return cur
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        current=Node(val)
        current.next=self.head
        self.head=current
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head==None:
            self.addAtHead(val)
        newNode=Node(val)
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=newNode
     
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index==0:
            self.addAtHead(val)

        prev=self.getNode(index-1)
        if prev is None:return 
        cur=Node(val)
        next_elt=prev.next
        cur.next=next_elt
        prev.next=cur
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        current=self.head
        i=0
        while (i<index-1 and self.head.next is not None):

            self.head = self.head.next
            i+=1
        self.head= self.head.next
       
        