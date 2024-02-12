class MyLinkedList:
    def __init__(self):
        self.head = self
        self.val = None
        self.next = None
           
    def get(self, index):
        current = self.head
        i = 0
        if self.head != None and self.head.val == None:
            return -1
        if index == 0 and self.head != None:
            return self.head.val
        while i < index and current != None:
            current = current.next
            i += 1
        if current == None:
            return -1
        else:
            return current.val

    def addAtHead(self, val):
        if self.val != None:
            newNode = MyLinkedList()
            newNode.val = val
            newNode.next = self.head
            self.head = newNode
        elif self.val == None:
            self.val = val
        
    def addAtTail(self, val):
        if self.val == None:
            self.val = val
            return
        addedValue = MyLinkedList()
        addedValue.val = val
        currentTail = self.head
        current = self.head
        while current != None:
            currentTail = current
            current = current.next
        currentTail.next = addedValue

    def addAtIndex(self, index, val) :
        addedValue = MyLinkedList()
        addedValue.val = val
        i = 0
        current = self.head
        if index == 0:
            self.addAtHead(val)
            return
        while current != None and i < index - 1:
            current = current.next
            i += 1
        if current != None:   
            currentNext = current.next
            current.next = addedValue
            addedValue.next = currentNext

    def deleteAtIndex(self, index):
        i = 0
        current = self.head
        prev = current
        if index == 0:
            self.head = self.head.next
            return
        while i < (index) and current != None:
            prev = current
            current = current.next
            i += 1
        if current != None and current.next == None:
            prev.next = None
        elif current != None:
            prev.next = current.next   
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)