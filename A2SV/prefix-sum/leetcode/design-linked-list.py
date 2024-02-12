class Node:
    def __init__(self):
        self.val = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.dummy.next
        i = 0
        while i < index:
            cur = cur.next
            i += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        print(ListNode())
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        prevNode = self.dummy
        i = 0
        while i < index:
            prevNode = prevNode.next
            i += 1
        prevNode.next = ListNode(val, prevNode.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prevNode = self.dummy
        i = 0
        while i < index:
            prevNode = prevNode.next
            i += 1

        tail = prevNode.next
        prevNode.next = tail.next
        tail.next = None 
        self.size -= 1